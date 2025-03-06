-- Get All Titles and their Genres including shows with no genre
SELECT s.title, g.name
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS j
ON s.id = j.show_id
LEFT JOIN tv_genres AS g
ON j.genre_id = g.id
ORDER BY s.title, g.name;
