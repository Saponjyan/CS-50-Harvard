SELECT distinct name
FROM people as p
JOIN directors as d ON p.id = d.person_id
JOIN ratings as r ON r.movie_id = d.movie_id
WHERE rating >= 9.0;