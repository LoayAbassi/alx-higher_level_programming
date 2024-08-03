-- lists genres and number of shows related to each one
SELECT tv_genres.name AS genre, count(tv_show_genres.show_id)
AS number_of_shows
FROM tv_genres,tv_show_genres 
WHERE tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;