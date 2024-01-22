-- SQL script that creates a trigger that resets the attribute
-- valid_email only when the email has been changed
DELIMITER //
CREATE TRIGGER emailValidator
BEFORE INSERT ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> (SELECT email FROM users WHERE name = NEW.name) THEN
        SET NEW.valid_email = 0;
    ELSE
        SET NEW.valid_email= 1;
    END IF;
END;//
DELIMITER ;
