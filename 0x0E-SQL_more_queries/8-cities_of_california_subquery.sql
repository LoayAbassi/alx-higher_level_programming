-- lists all cities of calefornia
SELECT id, name
FROM cities
WHERE state_id = (
      SELECT id
      FROM states
      WHERE name = 'California'
);