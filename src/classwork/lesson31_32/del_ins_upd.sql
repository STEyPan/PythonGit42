DELETE FROM personal WHERE id = '0f57d6df-94ef-4d50-9602-247eb369b4b3';

INSERT INTO personal (id, name, age) VALUES
	('0f57d6df-94ef-4d50-9602-247eb369b4b3', 'Гришков Михаил', 76)
	ON CONFLICT (id)
	DO UPDATE SET age = EXCLUDED.age, name = EXCLUDED.name;
	-- Исключения необходимы для обновления данных в полях

UPDATE personal SET name = 'Пример Примеров' WHERE name = 'Петров Петр';

SELECT * FROM personal;

-- INSERT INTO <название таблицы> (<список атрибутов>) - [если нужны определенные атрибуты] VALUES
-- (<значение одного элемента через запятую>),
-- (<значение одного элемента через запятую>),
-- (<значение одного элемента через запятую>),
-- (<значение одного элемента через запятую>)
-- ON CONFLICT (<поле по которому может возникнуть конфликт>)
-- DO UPDATE SET <какие поля заменить>;

-- Удаление значений:
-- DELETE FROM <название таблицы> WHERE <условие для выбора элемента>;

-- Изменение значений:
-- UPDATE <название таблицы> SET <что поменять> WHERE <у кого поменять>;