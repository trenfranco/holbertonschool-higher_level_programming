-- lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT s.title, g.genre_id
FROM tv_shows s LEFT JOIN tv_show_genres g
ON s.id = g.show_id
WHERE g.genre_id IS NULL
ORDER BY s.title, g.genre_id
