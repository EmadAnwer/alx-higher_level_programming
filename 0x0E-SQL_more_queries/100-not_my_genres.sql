-- not Dexter

SELECT tv_genres.name
FROM tv_genres
LEFT JOIN (SELECT tv_show_genres.genre_id AS id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter') AS Dexter_id
ON Dexter_id.id = tv_genres.id
WHERE Dexter_id.id IS NULL
ORDER BY tv_genres.name
