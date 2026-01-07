# **PostgreSQL Database Configuration**

This directory contains the configuration files for a PostgreSQL database. It includes SQL scripts for initialization, schema creation, views, and procedures, as well as a comprehensive test suite to verify the database's structure, permissions, and functionality.

## **Setup and Execution**

The database is initialized and configured using a single shell script.

1. **Configure Variables**: Ensure the .env file in the project's root directory is correctly configured with all necessary credentials.  
2. **Run the Script**: From the root directory, execute the following command:  
```./execute\_scripts.sh```

This script will read the variables from .env, process the SQL templates, and execute all scripts in the correct order to get the database ready for use.

## **File Structure**

* ```execute\_scripts.sh```: Orchestrates the entire initialization process.  
* ```scripts/```: Contains the SQL files.  
  * ```01-init-db.sql.template```: Creates the database and user roles.  
  * ```02-create-schema.sql```: Defines and creates all tables.  
  * ```03-views.sql```: Creates the database views.  
  * ```04-procediments.sql```: Creates stored functions and procedures.  
  * ```10-grant-permissions.sql.template```: Assigns specific permissions to each role.  
* ```test/```: Contains the pytest tests.  
  * ```conftest.py```: Prepares the test environment (fixtures), including DB connection and data population/cleanup.  
  * ```test\_db\_setup.py```: Contains tests that verify the basic structure and role permissions.  
  * ```test\_db\_integrity.py```: Contains tests that verify data integrity (constraints, foreign keys, cascades).

## **Testing**

To run the tests, ensure you have the dependencies from requeriments.txt installed, and then run from the project's root directory:

```pytest \-v```

## **Database Schema**

### **Tables**

#### **USERS**

Stores information for registered users.

| Column | Type | Description |
| :---- | :---- | :---- |
| id | UUID | **Primary Key**, default `gen_random_uuid()`. Unique identifier. |
| email | VARCHAR(255) | **Unique**, **Not Null**. User's email. |
| hashed_password | VARCHAR(255) | **Not Null**. Password hash (stored hashed). |
| is_active | BOOLEAN | Default `TRUE`. User account active flag. |
| is_superuser | BOOLEAN | Default `FALSE`. Superuser flag. |
| is_verified | BOOLEAN | Default `FALSE`. Email/identity verification flag. |

#### **CHATS**

Stores conversations or chats, associated with a user.

| Column | Type | Description |
| :---- | :---- | :---- |
| id | UUID | **Primary Key**, default `gen_random_uuid()`. Unique chat identifier. |
| title | VARCHAR(255) | Title or name of the chat. |
| user_id | UUID | **Not Null**, **Foreign Key** to `users(id)`. `ON DELETE CASCADE`, `ON UPDATE CASCADE`. |

#### **IA_PROMPTS**

Stores system prompt templates for the AI.

| Column | Type | Description |
| :---- | :---- | :---- |
| id | UUID | **Primary Key**, default `gen_random_uuid()`. |
| prompt_name | TEXT | **Not Null**. Name of template. |
| prompt | TEXT | **Not Null**. The text of the system prompt. |
| prompt_description | TEXT | Description of the prompt's purpose. |
| AI_name | VARCHAR(255) | **Unique**, **Not Null**. Name for the prompt. |

#### **MODELS**

Stores the different available AI models.

| Column | Type | Description |
| :---- | :---- | :---- |
| id | UUID | **Primary Key**, default `gen_random_uuid()`. |
| AI_name | VARCHAR(255) | **Unique**, **Not Null**. Model name (e.g., 'GPT-4'). |

#### **MESSAGES**

Stores each individual message within a chat.

| Column | Type | Description |
| :---- | :---- | :---- |
| id | UUID | **Primary Key**, default `gen_random_uuid()`. |
| order_number | INTEGER | **Not Null**. Order of the message in the chat. **Unique** with `chat_id`. |
| content | TEXT | **Not Null**. The content of the message. |
| statistics | TEXT | Optional statistics for the message (stored as TEXT; may contain JSON). |
| chat_id | UUID | **Not Null**, **Foreign Key** to `chats(id)`. `ON DELETE CASCADE`, `ON UPDATE CASCADE`. |
| model_id | UUID | **Foreign Key** to `models(id)`. `ON DELETE RESTRICT`, `ON UPDATE RESTRICT`. |
| AI_prompt_id | UUID | **Foreign Key** to `ia_prompts(id)`. `ON DELETE RESTRICT`, `ON UPDATE RESTRICT`. |

Unique constraints and notes:

- The schema enforces `UNIQUE (chat_id, order_number)` to guarantee message ordering is unique within a chat.
- `pgcrypto` extension is enabled in the schema to provide `gen_random_uuid()` for UUID generation.

### **Views**

* **users_id_email_view**: A secure view (defined in `scripts/03-views.sql`) that exposes only `id` and `email` from the `users` table.

### **Functions**

* **get_user_id_by_email(user_email VARCHAR(255))**: (defined in `scripts/04-procediments.sql`) returns the UUID of the user matching the given email by querying `users_id_email_view`. Raises an exception if no user is found.

## **.env Environment Variables**

### **PostgreSQL Variables**

Used by the official PostgreSQL image.

* POSTGRES\_PASSWORD: Password for the postgres superuser.  
* POSTGRES\_USER: Name of the superuser (default is postgres).

### **Custom Variables**

Used by the initialization scripts.

* APP\_DB\_NAME: The name of the application database (e.g., diligencia).  
* DB\_OWNER\_USER: The role that owns the database and all its objects.  
* DB\_OWNER\_PASSWORD: Password for the owner role.  
* APP\_USER: The role the main application will use for its operations (reading/writing chats, etc.).  
* APP\_USER\_PASSWORD: Password for the APP\_USER role.  
* APP\_USER\_LOGIN: A specific role for account management (reading/writing to the USERS table).  
* APP\_USER\_LOGIN\_PASSWORD: Password for the APP\_USER\_LOGIN role.