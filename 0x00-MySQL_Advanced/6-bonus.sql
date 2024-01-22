-- SQL script that creates a stored procedure AddBonus
-- that adds a new correction for a student
CREATE PROCEDURE AddBonus(
IN user_id INT,
IN project_name VARCHAR(255),
IN score INT
)
BEGIN
    DECLARE project_id INT;
    SELECT id INTO project_id FROM projects WHERE name = NEW.name LIMIT 1;
    IF NEW.project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (NEW.name);
        SET project_id = LAST_INSERT_ID();
    END IF;
    INSERT INTO corrections (user_id, project_id, score) VALUES (USer_id, project_id, score);
END //
