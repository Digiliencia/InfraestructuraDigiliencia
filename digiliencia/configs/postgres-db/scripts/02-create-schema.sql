-- Optional: Drop tables if they exist (useful for development)
DROP TABLE IF EXISTS MENSAJE;
DROP TABLE IF EXISTS CHATS;
DROP TABLE IF EXISTS USUARIO;
DROP TABLE IF EXISTS IA_PROMPTS;
DROP TABLE IF EXISTS MODELO;


-- Create the USUARIO table
CREATE TABLE USUARIO (
    ID SERIAL PRIMARY KEY, -- SERIAL automatically creates a sequence and provides unique integer IDs
    email VARCHAR(255) UNIQUE NOT NULL, -- Email should be unique and not null
    password VARCHAR(255) NOT NULL -- Password should not be null
);

-- Create the CHATS table
CREATE TABLE CHATS (
    ID SERIAL PRIMARY KEY,
    titulo VARCHAR(255),
    usuario_id INTEGER NOT NULL REFERENCES USUARIO(ID) ON DELETE CASCADE ON UPDATE CASCADE -- Foreign key linking chats to users, cascade on delete/update
);

-- Create the IA_PROMPTS table
CREATE TABLE IA_PROMPTS (
    ID SERIAL PRIMARY KEY,
    prompt TEXT NOT NULL, -- Use TEXT for potentially longer prompt strings
    descripcion TEXT,
    nombre VARCHAR(255) UNIQUE NOT NULL -- Assuming prompt names should be unique
);

-- Create the MODELO table
CREATE TABLE MODELO (
    ID SERIAL PRIMARY KEY,
    nombre VARCHAR(255) UNIQUE NOT NULL -- Assuming model names should be unique
);

-- Create the MENSAJE table
CREATE TABLE MENSAJE (
    ID SERIAL PRIMARY KEY,
    numero INTEGER NOT NULL, -- Message number within a chat
    contenido TEXT NOT NULL,
    estadisticas TEXT, -- Use TEXT for potential JSON or other string data for stats
    chat_id INTEGER NOT NULL REFERENCES CHATS(ID) ON DELETE CASCADE ON UPDATE CASCADE, -- Foreign key linking messages to chats, cascade on delete/update
    modelo_id INTEGER REFERENCES MODELO(ID) ON DELETE RESTRICT ON UPDATE RESTRICT, -- Foreign key linking message to a model, restrict delete/update if messages exist
    ia_prompt_id INTEGER REFERENCES IA_PROMPTS(ID) ON DELETE RESTRICT ON UPDATE RESTRICT, -- Foreign key linking message to a prompt, restrict delete/update if messages exist

    -- Add a unique constraint to ensure message number is unique within a chat
    UNIQUE (chat_id, numero)
);