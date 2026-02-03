-- 01-init-db.sql

-- Clean up existing tables (Order matters due to Foreign Keys)
DROP TABLE IF EXISTS messages CASCADE;
DROP TABLE IF EXISTS chats CASCADE;
DROP TABLE IF EXISTS ai_prompts CASCADE;
DROP TABLE IF EXISTS models CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- Enable pgcrypto for UUID generation
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- 1. USERS Table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    is_superuser BOOLEAN DEFAULT FALSE,
    is_verified BOOLEAN DEFAULT FALSE
);

-- 2. AI_PROMPTS Table
CREATE TABLE ai_prompts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL UNIQUE,
    prompt_text TEXT NOT NULL,
    description TEXT
);

-- 3. MODELS Table
CREATE TABLE models (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) UNIQUE NOT NULL
);

-- 4. CHATS Table
CREATE TABLE chats (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(255),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    ai_prompt_id UUID REFERENCES ai_prompts(id) ON DELETE SET NULL
);

-- 5. MESSAGES Table
CREATE TABLE messages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    order_number INTEGER NOT NULL,
    content TEXT NOT NULL,
    statistics JSONB,
    chat_id UUID NOT NULL REFERENCES chats(id) ON DELETE CASCADE,
    model_id UUID REFERENCES models(id) ON DELETE SET NULL,

    -- Ensure message ordering is unique per chat
    UNIQUE (chat_id, order_number)
);

-- --- OPTIONAL: SEED DATA (Initial data for the API to work) ---

-- Insert default AI Models
INSERT INTO models (name) VALUES ('qwen3:4b');
INSERT INTO models (name) VALUES ('test-model');

-- Insert default AI Prompts (Templates)
INSERT INTO ai_prompts (name, prompt_text, description) 
VALUES (
    'General Assistant', 
    'You are a helpful and polite AI assistant.', 
    'Standard assistant for general queries.'
);

INSERT INTO ai_prompts (name, prompt_text, description) 
VALUES (
    'Code Expert', 
    'You are an expert software engineer. You prefer clean code and Python.', 
    'Assistant specialized in programming tasks.'
);