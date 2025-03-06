-- Lists the cities of California that can be found in the DB hbtn_0d_usa
SELECT cities.id, cities.name
FROM cities, states
WHERE states.name = "California"
ORDER BY cities.id;
