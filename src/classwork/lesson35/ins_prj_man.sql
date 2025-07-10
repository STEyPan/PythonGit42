INSERT INTO project_manager (name, birthday, telephone, salary) VALUES
	('Петров Игорь Николаевич','1974.02.22','8(980)492-26-22', 150000),
	('Сидоров Алексей Владимирович', '1985-05-15', '8(910)123-45-67', 180000),
    ('Иванова Мария Сергеевна', '1990-11-30', '8(915)987-65-43', 200000),
    ('Кузнецов Дмитрий Александрович', '1982-07-20', '8(920)456-78-90', 170000)

ON CONFLICT (telephone) DO UPDATE
SET salary = EXCLUDED.salary;	

SELECT * FROM project_manager;