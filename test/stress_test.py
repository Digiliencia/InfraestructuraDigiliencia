#!/usr/bin/env python3
"""
Stress Test for Chat API

Usage:
    python stress_test.py --users 10 --duration 300 --api-url http://localhost:8000/api

Parameters:
    --users: Number of concurrent users to simulate
    --duration: Duration of the test in seconds
    --api-url: Base API URL (e.g., http://localhost:8000/api)
"""

import argparse
import asyncio
import random
import string
import time
from datetime import datetime
from typing import Optional

import httpx


# ----------------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------------

SAMPLE_QUESTIONS = [
    "¿Cuál es la capital de Francia?",
    "Explícame qué es la fotosíntesis",
    "¿Quién escribió Don Quijote?",
    "Dame una receta de paella",
    "¿Cuántos planetas hay en el sistema solar?",
    "Explícame la teoría de la relatividad",
    "¿Qué es el ADN?",
    "Cuéntame sobre la historia de España",
    "¿Cómo funcionan los ordenadores?",
    "Dame consejos para aprender inglés",
]

CHAT_TITLES = [
    "Conversación general",
    "Preguntas variadas",
    "Consultas",
    "Chat de prueba",
    "Sesión de aprendizaje",
]


# ----------------------------------------------------------------------------
# Helper Functions
# ----------------------------------------------------------------------------

def generate_random_string(length: int = 8) -> str:
    """Generate a random string for usernames."""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


def generate_secure_password(length: int = 12) -> str:
    """
    Generate a secure password with:
    - At least 8 characters (default 12)
    - Uppercase letters
    - Lowercase letters
    - Numbers
    - Special characters
    """
    if length < 8:
        length = 8
    
    # Ensure at least one of each required character type
    password_chars = [
        random.choice(string.ascii_uppercase),  # At least 1 uppercase
        random.choice(string.ascii_lowercase),  # At least 1 lowercase
        random.choice(string.digits),           # At least 1 digit
        random.choice("!@#$%^&*()_+-=[]{}"),   # At least 1 special char
    ]
    
    # Fill the rest with random mix
    all_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%^&*()_+-=[]{}|~"
    password_chars.extend(random.choices(all_chars, k=length - 4))
    
    # Shuffle to avoid predictable pattern
    random.shuffle(password_chars)
    
    return ''.join(password_chars)


def log(user_id: int, message: str):
    """Log a message with timestamp and user ID."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] User#{user_id:03d}: {message}")


# ----------------------------------------------------------------------------
# User Simulator
# ----------------------------------------------------------------------------

class UserSimulator:
    """Simulates a single user interacting with the Chat API."""
    
    def __init__(self, user_id: int, api_url: str, duration: int):
        self.user_id = user_id
        self.api_url = api_url.rstrip('/')
        self.duration = duration
        self.username = f"stresstest_{generate_random_string(8)}"
        self.password = generate_secure_password(12)
        self.email = f"{self.username}@example.com"
        self.token: Optional[str] = None
        self.chat_id: Optional[str] = None
        self.models: list = []
        self.client = httpx.AsyncClient(timeout=60.0, verify=False)
        
    async def run(self):
        """Main execution flow for a user."""
        start_time = time.time()
        
        try:
            # 1. Register
            if not await self.register():
                return
            
            # 2. Login
            if not await self.login():
                return
            
            # 3. Get available models
            await self.fetch_models()
            
            # 4. Create chat
            if not await self.create_chat():
                return
            
            # 5. Send messages until duration expires
            message_count = 0
            while time.time() - start_time < self.duration:
                await self.send_message()
                message_count += 1
                
                # Random delay between messages (2-10 seconds)
                await asyncio.sleep(random.uniform(2, 10))
            
            log(self.user_id, f"✅ Completed! Sent {message_count} messages")
            
        except Exception as e:
            log(self.user_id, f"❌ Error: {e}")
        
        finally:
            # Cleanup: Delete user account
            await self.cleanup()
            await self.client.aclose()
    
    async def register(self) -> bool:
        """Register a new user account."""
        try:
            payload = {
                "email": self.email,
                "password": self.password,
                "username": self.username,
            }
            
            response = await self.client.post(
                f"{self.api_url}/auth/register",
                json=payload
            )
            
            if response.status_code in [200, 201]:
                log(self.user_id, f"✓ Registered as {self.username}")
                return True
            else:
                # Show detailed error for debugging
                error_detail = ""
                try:
                    error_data = response.json()
                    error_detail = f" - {error_data}"
                except:
                    error_detail = f" - {response.text[:100]}"
                
                log(self.user_id, f"✗ Registration failed: {response.status_code}{error_detail}")
                return False
                
        except Exception as e:
            log(self.user_id, f"✗ Registration error: {e}")
            return False
    
    async def login(self) -> bool:
        """Login and obtain JWT token."""
        try:
            response = await self.client.post(
                f"{self.api_url}/auth/login",
                json={
                    "email": self.email,
                    "password": self.password,
                }
            )
            
            if response.status_code == 200:
                data = response.json()
                self.token = data.get("access_token")
                
                if self.token:
                    # Set auth header for future requests
                    self.client.headers["Authorization"] = f"Bearer {self.token}"
                    log(self.user_id, "✓ Logged in")
                    return True
            
            log(self.user_id, f"✗ Login failed: {response.status_code}")
            return False
            
        except Exception as e:
            log(self.user_id, f"✗ Login error: {e}")
            return False
    
    async def fetch_models(self):
        """Fetch available AI models."""
        try:
            response = await self.client.get(f"{self.api_url}/chats/models")
            
            if response.status_code == 200:
                data = response.json()
                self.models = data.get("models", [])
                log(self.user_id, f"✓ Found {len(self.models)} models")
            else:
                log(self.user_id, f"⚠ Could not fetch models, will use default")
                
        except Exception as e:
            log(self.user_id, f"⚠ Model fetch error: {e}")
    
    async def create_chat(self) -> bool:
        """Create a new chat conversation."""
        try:
            response = await self.client.patch(
                f"{self.api_url}/chats",
                json={
                    "title": random.choice(CHAT_TITLES),
                }
            )
            
            if response.status_code in [200, 201]:
                data = response.json()
                self.chat_id = data.get("id")
                log(self.user_id, f"✓ Created chat {self.chat_id}")
                return True
            else:
                log(self.user_id, f"✗ Chat creation failed: {response.status_code}")
                return False
                
        except Exception as e:
            log(self.user_id, f"✗ Chat creation error: {e}")
            return False
    
    async def send_message(self):
        """Send a message to the chat."""
        try:
            question = random.choice(SAMPLE_QUESTIONS)
            
            # Select random model if available
            model_id = None
            if self.models:
                model = random.choice(self.models)
                model_id = model.get("id")
            
            payload = {
                "content": question,
            }
            
            if model_id:
                payload["model_id"] = model_id
            
            response = await self.client.patch(
                f"{self.api_url}/chats/{self.chat_id}",
                json=payload
            )
            
            if response.status_code == 200:
                log(self.user_id, f"✓ Message sent: '{question[:30]}...'")
            else:
                log(self.user_id, f"✗ Message failed: {response.status_code}")
                
        except Exception as e:
            log(self.user_id, f"✗ Message error: {e}")
    
    async def cleanup(self):
        """Delete user account."""
        try:
            response = await self.client.delete(f"{self.api_url}/users/me")
            
            if response.status_code in [200, 204]:
                log(self.user_id, "✓ User deleted")
            else:
                log(self.user_id, f"⚠ User deletion failed: {response.status_code}")
                
        except Exception as e:
            log(self.user_id, f"⚠ Cleanup error: {e}")


# ----------------------------------------------------------------------------
# Main Test Runner
# ----------------------------------------------------------------------------

async def run_stress_test(num_users: int, duration: int, api_url: str):
    """Run the stress test with the specified parameters."""
    
    print("\n" + "=" * 70)
    print("🔥 CHAT API STRESS TEST")
    print("=" * 70)
    print(f"API URL:       {api_url}")
    print(f"Users:         {num_users}")
    print(f"Duration:      {duration} seconds ({duration // 60} minutes)")
    print(f"Start time:    {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70 + "\n")
    
    # Create user simulators
    users = [
        UserSimulator(user_id=i + 1, api_url=api_url, duration=duration)
        for i in range(num_users)
    ]
    
    # Calculate stagger delay: spread user creation over first 20% of test duration
    # or max 60 seconds, whichever is smaller
    max_stagger_time = min(duration * 0.2, 60)
    stagger_delay = max_stagger_time / num_users if num_users > 1 else 0
    
    print(f"ℹ️  Users will be created gradually over {max_stagger_time:.1f} seconds")
    print(f"   (one user every ~{stagger_delay:.1f} seconds)\n")
    
    # Start users with staggered delays
    async def start_user_with_delay(user: UserSimulator, delay: float):
        """Start a user after a delay to simulate gradual arrival."""
        await asyncio.sleep(delay)
        await user.run()
    
    start_time = time.time()
    tasks = [
        start_user_with_delay(user, i * stagger_delay)
        for i, user in enumerate(users)
    ]
    
    # Run all users concurrently (but with staggered starts)
    await asyncio.gather(*tasks)
    elapsed = time.time() - start_time
    
    print("\n" + "=" * 70)
    print("✅ STRESS TEST COMPLETED")
    print("=" * 70)
    print(f"Total time:    {elapsed:.2f} seconds ({elapsed / 60:.1f} minutes)")
    print(f"End time:      {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70 + "\n")


# ----------------------------------------------------------------------------
# CLI Entry Point
# ----------------------------------------------------------------------------

def main():
    """Parse arguments and run the stress test."""
    parser = argparse.ArgumentParser(
        description="Stress test for Chat API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Test with 10 users for 5 minutes
  python stress_test.py --users 10 --duration 300 --api-url http://localhost:8000/api
  
  # Test with 50 users for 30 minutes
  python stress_test.py --users 50 --duration 1800 --api-url https://api.example.com/api
        """
    )
    
    parser.add_argument(
        "--users",
        type=int,
        required=True,
        help="Number of concurrent users to simulate"
    )
    
    parser.add_argument(
        "--duration",
        type=int,
        required=True,
        help="Test duration in seconds"
    )
    
    parser.add_argument(
        "--api-url",
        type=str,
        required=True,
        help="Base API URL (e.g., http://localhost:8000/api)"
    )
    
    args = parser.parse_args()
    
    # Validate parameters
    if args.users < 1:
        print("Error: --users must be at least 1")
        return
    
    if args.duration < 10:
        print("Error: --duration must be at least 10 seconds")
        return
    
    # Run the test
    try:
        asyncio.run(run_stress_test(args.users, args.duration, args.api_url))
    except KeyboardInterrupt:
        print("\n\n⚠ Test interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Test failed: {e}")


if __name__ == "__main__":
    main()
