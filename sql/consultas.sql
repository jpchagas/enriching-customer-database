use rbsdb;

select gender,COUNT(*) from people p2 group by gender

select a.city,p.gender ,COUNT(*) from people p inner join address a on p.id = a.pessoa_id GROUP BY a.city, p.gender 

SELECT * FROM people p 