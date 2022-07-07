-- lists all the cities of California
SELECT c.id, c.name 
FROM states s, cities c 
WHERE 
	s.name = "California" AND c.state_id = s.id
ORDER  BY c.id ASC
