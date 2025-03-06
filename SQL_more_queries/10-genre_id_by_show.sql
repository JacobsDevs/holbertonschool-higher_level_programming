-- Select Show's titles and their Genre ID where the genre_id is not null.
-- Order by Show's title first, then Genre ID.
SELECT s.title, g.genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g
ON s.id = g.show_id 
WHERE g.show_id IS NOT NULL 
ORDER BY s.title, g.genre_id;
