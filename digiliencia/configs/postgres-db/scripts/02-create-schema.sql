-- Optional: Drop tables if they exist (useful for development)
DROP TABLE IF EXISTS MESSAGES CASCADE;
DROP TABLE IF EXISTS CHATS CASCADE;
DROP TABLE IF EXISTS USERS CASCADE;
DROP TABLE IF EXISTS IA_PROMPTS CASCADE;
DROP TABLE IF EXISTS MODELS CASCADE;


-- Create the USERS table
-- Note: Adjusted to match FastAPI Users requirements
CREATE TABLE users (
    id SERIAL PRIMARY KEY,                -- SERIAL automatically creates a sequence and provides unique integer IDs
    email VARCHAR(255) UNIQUE NOT NULL,    -- Email should be unique and not null
    hashed_password VARCHAR(255) NOT NULL,        -- Password should not be null (hashed password)
    is_active BOOLEAN DEFAULT TRUE,        -- User's account active status (default is TRUE)
    is_superuser BOOLEAN DEFAULT FALSE,    -- User's superuser status (default is FALSE)
    is_verified BOOLEAN DEFAULT FALSE     -- User's verification status (default is FALSE)
);

-- Create the CHATS table
CREATE TABLE CHATS (
    ID SERIAL PRIMARY KEY,
    titulo VARCHAR(255),
    user_id INTEGER NOT NULL REFERENCES USERS(ID) ON DELETE CASCADE ON UPDATE CASCADE -- Foreign key linking chats to users, cascade on delete/update
);

-- Create the IA_PROMPTS table
CREATE TABLE IA_PROMPTS (
    ID SERIAL PRIMARY KEY,
    prompt TEXT NOT NULL, -- Use TEXT for potentially longer prompt strings
    prompt_description TEXT,
    IA_name VARCHAR(255) UNIQUE NOT NULL -- Assuming prompt names should be unique
);

-- Create the MODELS table
CREATE TABLE MODELS (
    ID SERIAL PRIMARY KEY,
    IA_name VARCHAR(255) UNIQUE NOT NULL -- Assuming model names should be unique
);

-- Create the MESSAGES table
CREATE TABLE MESSAGES (
    ID SERIAL PRIMARY KEY,
    order_number INTEGER NOT NULL, -- Message number within a chat
    content TEXT NOT NULL,
    statistics TEXT, -- Use TEXT for potential JSON use JSONB
    chat_id INTEGER NOT NULL REFERENCES CHATS(ID) ON DELETE CASCADE ON UPDATE CASCADE, -- Foreign key linking messages to chats, cascade on delete/update
    model_id INTEGER REFERENCES MODELS(ID) ON DELETE RESTRICT ON UPDATE RESTRICT, -- Foreign key linking message to a model, restrict delete/update if messages exist
    ia_prompt_id INTEGER REFERENCES IA_PROMPTS(ID) ON DELETE RESTRICT ON UPDATE RESTRICT, -- Foreign key linking message to a prompt, restrict delete/update if messages exist

    -- Add a unique constraint to ensure message number is unique within a chat
    UNIQUE (chat_id, order_number)
);
