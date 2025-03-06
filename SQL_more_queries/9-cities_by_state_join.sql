-- Select all cities in the DB with their states.
SELECT c.id, c.name, s.name
FROM cities AS c 
LEFT JOIN states AS s
ON c.state_id = s.id;
