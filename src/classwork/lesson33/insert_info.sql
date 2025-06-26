INSERT INTO groups VALUES
	-- ('bfd28ea4-dc7e-4a91-9575-eab00dfa41d0','Py42','очная'),
	-- ('e368bdf9-c264-4649-b8d4-b7c9f7b11521','Py111','очная'),
	-- ('ab0497cc-d66d-4601-885b-8ae7b8267ba7','BV12','очная'),
	('09644f79-9a27-46a5-9f9c-d38b7eb175fe','GR15','очная')

INSERT INTO students VALUES
	-- ('ad8103ab-cd00-43b7-979a-cb859ea3d3c2','Дима',20,4.5,'bfd28ea4-dc7e-4a91-9575-eab00dfa41d0'),
	-- ('28938a42-8c4c-4925-b25b-b7a158a2416b','Вася',25,4.5,'bfd28ea4-dc7e-4a91-9575-eab00dfa41d0'),
	-- ('8fa27dda-86d9-43b7-aaaf-883102be99b3','Михаил',28,4.5,'e368bdf9-c264-4649-b8d4-b7c9f7b11521'),
	-- ('4f942a62-a61b-4629-b3eb-0e1cd55ed314','Петя',22,4.5,'ab0497cc-d66d-4601-885b-8ae7b8267ba7'),
	-- ('97406240-14c8-409f-b435-9fecbcd39a19','Маша',35,4.5,'e368bdf9-c264-4649-b8d4-b7c9f7b11521'),
	-- ('943e5f7e-8a46-4066-b080-5b3e2e4a1205','Лена',24,4.5,'ab0497cc-d66d-4601-885b-8ae7b8267ba7'),
	-- ('8c1a70ee-5d6b-471f-99d8-03a6ed02cc37','Даша',20,4.5,'09644f79-9a27-46a5-9f9c-d38b7eb175fe'),
	-- ('20b107d8-e672-488f-9590-eb91ba5ca11c','Саша',21,4.5,'09644f79-9a27-46a5-9f9c-d38b7eb175fe'),
	-- ('20faa7b1-689b-42ff-a9b6-cfe62cb84a14','Коля',25,4.5,'bfd28ea4-dc7e-4a91-9575-eab00dfa41d0')
	-- ON CONFLICT (id)
	-- DO UPDATE SET gr=EXCLUDED.gr;

UPDATE students
SET grade = 4.8
WHERE name = 'Саша';

SELECT * FROM groups;
SELECT * FROM students;

-- DELETE FROM groups WHERE id = '09644f79-9a27-46a5-9f9c-d38b7eb175fe';