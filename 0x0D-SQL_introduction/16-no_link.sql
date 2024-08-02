-- lists record of names and scores(base of order)
--without counting names with no value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ""
ORDER BY score DESC;