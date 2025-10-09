-- Optional: Drop tables if they exist (useful for development)
DROP TABLE IF EXISTS MESSAGES CASCADE;
DROP TABLE IF EXISTS CHATS CASCADE;
DROP TABLE IF EXISTS USERS CASCADE;
DROP TABLE IF EXISTS IA_PROMPTS CASCADE;
DROP TABLE IF EXISTS MODELS CASCADE;

CREATE EXTENSION IF NOT EXISTS pgcrypto;  -- enable pgcrypto for gen_random_uuid()

-- Create the USERS table
-- Note: Adjusted to match FastAPI Users requirements
CREATE TABLE USERS (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),                -- SERIAL automatically creates a sequence and provides unique integer IDs
    email VARCHAR(255) UNIQUE NOT NULL,    -- Email should be unique and not null
    hashed_password VARCHAR(255) NOT NULL,        -- Password should not be null (hashed password)
    is_active BOOLEAN DEFAULT TRUE,        -- User's account active status (default is TRUE)
    is_superuser BOOLEAN DEFAULT FALSE,    -- User's superuser status (default is FALSE)
    is_verified BOOLEAN DEFAULT FALSE     -- User's verification status (default is FALSE)
);

-- Create the IA_PROMPTS table
CREATE TABLE IA_PROMPTS (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    prompt_name VARCHAR(255) NOT NULL,
    prompt TEXT NOT NULL, -- Use TEXT for potentially longer prompt strings
    prompt_description TEXT
);
-- Create the CHATS table
CREATE TABLE CHATS (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tittle VARCHAR(255),
    user_id UUID NOT NULL REFERENCES USERS(ID) ON DELETE CASCADE ON UPDATE CASCADE, -- Foreign key linking chats to users, cascade on delete/update
    ia_prompt_id UUID REFERENCES IA_PROMPTS(ID) ON DELETE RESTRICT ON UPDATE RESTRICT -- Foreign key linking chat to a prompt
);


-- Create the MODELS table
CREATE TABLE MODELS (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    IA_name VARCHAR(255) UNIQUE NOT NULL -- Assuming model names should be unique
);

-- Create the MESSAGES table
CREATE TABLE MESSAGES (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    order_number INTEGER NOT NULL, -- Message number within a chat
    content TEXT NOT NULL,
    statistics TEXT, -- Use TEXT for potential JSON use JSONB
    chat_id UUID NOT NULL REFERENCES CHATS(ID) ON DELETE CASCADE ON UPDATE CASCADE, -- Foreign key linking messages to chats, cascade on delete/update
    model_id UUID REFERENCES MODELS(ID) ON DELETE RESTRICT ON UPDATE RESTRICT, -- Foreign key linking message to a model, restrict delete/update if messages exist

    -- Add a unique constraint to ensure message number is unique within a chat
    UNIQUE (chat_id, order_number)
);
