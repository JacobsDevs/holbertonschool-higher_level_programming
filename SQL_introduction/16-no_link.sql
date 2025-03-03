-- List all records in second_table that have a name.
SELECT score, name
FROM second_table
WHERE name != 'NULL'
ORDER BY score desc;
