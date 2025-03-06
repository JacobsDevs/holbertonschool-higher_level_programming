-- Select all shows Titles belonging to the Comedy Genre
SELECT title
FROM tv_shows
LEFT JOIN tv_show_genres AS j
ON j.show_id = tv_shows.id
LEFT JOIN tv_genres AS g
ON g.id = j.genre_id
WHERE g.name = "Comedy"
ORDER BY title;

