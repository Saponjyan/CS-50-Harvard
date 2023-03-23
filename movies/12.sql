select m.title
from movies AS m
join stars AS s on s.movie_id = m.id
join people AS p on p.id = s.person_id
where p.name in ('Johnny Depp', 'Helena Bonham Carter')
group by m.title
having Count(*) = 2;