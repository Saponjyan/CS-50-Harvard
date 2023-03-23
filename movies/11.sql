SELECT title
FROM movies as m
JOIN ratings as r ON m.id = r.movie_id
JOIN stars AS s ON r.movie_id = s.movie_id
JOIN people AS p ON p.id =s.person_id
WHERE name = 'Chadwick Boseman'
ORDER BY rating DESC
LIMIT 5;