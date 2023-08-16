-- INNER JOIN 

SELECT (tv_genres.name) AS genre , COUNT(tv_genres.name) AS number_of_shows
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY COUNT(tv_genres.name) DESC
