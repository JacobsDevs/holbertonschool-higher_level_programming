-- Select cities that are in California
SELECT c.id, c.name 
FROM cities as c 
WHERE c.state_id = (
	SELECT s.id 
	FROM states as s 
	WHERE s.name = "California")
ORDER BY c.id;
