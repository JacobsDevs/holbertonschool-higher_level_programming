-- Lists the cities of California that can be found in the DB hbtn_0d_usa
SELECT cities.id, cities.name 
FROM (
	SELECT * FROM cities AS cities
	UNION
	SELECT * FROM states AS states
)
WHERE states.name = "California"
ORDER BY cities.id;
