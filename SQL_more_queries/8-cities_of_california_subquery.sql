-- Lists the cities of California that can be found in the DB hbtn_0d_usa
SELECT cities.a.id, cities.a.name FROM (
	SELECT id, name FROM cities as cities
	UNION
	SELECT * FROM states as states
) as a
WHERE states.a.name = "California"
ORDER BY cities.a.id;
