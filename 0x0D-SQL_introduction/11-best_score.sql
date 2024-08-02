-- lists all records <= 10 based on score desc order
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;