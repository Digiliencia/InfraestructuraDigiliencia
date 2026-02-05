import asyncio
from digiliencia.configs.env import env
from digiliencia.fastAPI.core.agent_manager import agent_manager


async def periodic_cleanup():
    """Background task to periodically clean up inactive agent sessions."""
    interval_minutes = env.agent_cleanup_interval_minutes

    while True:
        try:
            await asyncio.sleep(interval_minutes * 60)  # Convert to seconds
            cleaned = agent_manager.cleanup_inactive_sessions()
            if cleaned > 0:
                print(f"[Background] Cleaned up {cleaned} inactive agent session(s)")
        except asyncio.CancelledError:
            print("[Background] Cleanup task cancelled")
            break
        except Exception as e:
            print(f"[Background] Error in cleanup task: {e}")
