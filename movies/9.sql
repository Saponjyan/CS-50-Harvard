SELECT name
FROM people as p
WHERE p.id IN
(SELECT  DISTINCT person_id
FROM stars AS s
JOIN movies as m ON s.movie_id = m.id
WHERE m.year = 2004)
ORDER BY birth;