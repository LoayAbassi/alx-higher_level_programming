-- Lists all genres not related to Dexter's show
SELECT tg.name
FROM tv_genres tg
WHERE tg.id NOT IN (
    SELECT tsg.genre_id
    FROM tv_show_genres tsg
    JOIN tv_shows ts ON tsg.show_id = ts.id
    WHERE ts.title = "Dexter"
)
ORDER BY tg.name;
