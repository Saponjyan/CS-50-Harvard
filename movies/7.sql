SELECT title, rating
from movies as m
JOIN ratings as r ON r.movie_id = m.id
where m.year = 2010
AND rating IS NOT NULL
ORDER BY rating DESC,title;