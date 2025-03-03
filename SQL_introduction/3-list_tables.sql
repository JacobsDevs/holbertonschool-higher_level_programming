-- List all the tables in passed database
SELECT table_name FROM information_schema.tables
WHERE table_schema = '@v1';
