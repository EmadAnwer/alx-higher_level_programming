-- Not my genre
SELECT tv_genres.name FROM tv_genres 
WHERE id NOT IN (
	SELECT tv_show_genres.genre_id
	FROM tv_shows
	INNER JOIN tv_show_genres
	ON tv_show_genres.show_id =  tv_shows.id
	WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name
