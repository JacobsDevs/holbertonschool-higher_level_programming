-- Select all the Genre names belonging to Dexter
SELECT name
FROM tv_genres
LEFT JOIN tv_show_genres AS j
ON tv_genres.id = j.genre_id
LEFT JOIN tv_shows AS t
ON t.id = j.show_id
WHERE t.title = "Dexter"
ORDER BY name;
