--  lists all shows contained in the database
SELECT s.title, g.genre_id
FROM tv_shows s LEFT JOIN tv_show_genres g
ON s.id = g.genre_id
ORDER BY s.title, g.genre_id ASC
