-- lists all genres of show Dexter
SELECT tv_genres.name
FROM tv_genres,tv_shows,tv_show_genres
WHERE
tv_genres.id = tv_show_genres.genre_id
AND
tv_show_genres.show_id = tv_shows.id
AND
tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;