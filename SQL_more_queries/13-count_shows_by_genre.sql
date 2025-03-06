-- Select the names of Genres and the count of shows in that genre.
SELECT g.name, COUNT(s.title) AS number_of_shows
FROM tv_genres AS g
LEFT JOIN tv_show_genres AS j
ON g.id = j.genre_id
LEFT JOIN tv_shows AS s
ON s.id = j.show_id
GROUP BY g.name
HAVING COUNT(s.title) > 0
ORDER BY number_of_shows DESC;
