CREATE OR REPLACE FUNCTION get_user_id_by_email(user_email VARCHAR(255))
RETURNS INTEGER AS $$
DECLARE
    user_id INTEGER;
BEGIN
    SELECT ID INTO user_id
    FROM users_id_email_view
    WHERE email = user_email;

    IF user_id IS NULL THEN
        RAISE EXCEPTION 'No user found with email %', user_email;
    END IF;

    RETURN user_id;
END;
$$ LANGUAGE plpgsql;
