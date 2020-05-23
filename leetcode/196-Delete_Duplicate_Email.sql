# DELETE FROM Person GROUP BY Email HAVING(COUNT(Email) > 1);

DELETE b FROM Person a, Person b WHERE a.Email = b.Email AND a.Id < b.Id;
