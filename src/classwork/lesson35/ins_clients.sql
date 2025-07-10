INSERT INTO clients (name, contact, telephone, price) VALUES
	('ООО Газпром','Гирева Галина Ивановна','8(980)643-28-76', 2000000),
	('Яндекс','Кулев Иван Дмитриевич','8(999)720-34-72', 4000000),
	('Правительство Ярославля','Носкова Анна Владимировна','8(920)244-30-42', 1500000)
	
ON CONFLICT (telephone) DO UPDATE
SET price = EXCLUDED.price;

-- DELETE FROM clients WHERE client_id = 'db126f6a-0f00-4397-9ee8-a09b61dbdd3d';


SELECT * FROM clients;