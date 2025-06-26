-- SELECT name, age, grade FROM students WHERE age > 20 OR name = 'Михаил';

-- SELECT students.name, age, grade, groups.name as group FROM students, groups
-- 	WHERE students.gr = groups.id AND groups.name ILIKE 'py42';

SELECT students.name as student, age, grade, groups.name as group 
	FROM groups, students
	WHERE groups.id = students.gr; --AND groups.name ILIKE 'py42';


	

