SELECT COUNT(*) AS "Количество овощей"
FROM veg_and_fru
WHERE type = 'Овощ';

SELECT COUNT(*) AS "Количество фруктов"
FROM veg_and_fru
WHERE type = 'Фрукт';

SELECT COUNT(*) AS "Кол-во Ф и О - зеленого цвета"
FROM veg_and_fru
WHERE type IN ('Фрукт','Овощ') and color ILIKE 'зеленый';

SELECT color AS "Цвет", COUNT(*) AS "Количество"
FROM veg_and_fru
GROUP BY color;

SELECT color AS "Цвет", COUNT(*) AS "MIN кол-во"
FROM veg_and_fru
GROUP BY color
ORDER BY COUNT(*) ASC
LIMIT 1;

SELECT color AS "Цвет", COUNT(*) AS "MAX кол-во"
FROM veg_and_fru
GROUP BY color
ORDER BY COUNT(*) DESC
LIMIT 1;

SELECT MIN(calorie) AS "MIN калории"
FROM veg_and_fru;

SELECT name, calorie AS "MIN калории"
FROM veg_and_fru
WHERE calorie = (SELECT MIN(calorie) FROM veg_and_fru);

SELECT name, calorie AS "MAX калории"
FROM veg_and_fru
WHERE calorie = (SELECT MAX(calorie) FROM veg_and_fru);

SELECT AVG(calorie) AS "Средняя калорийность"
FROM veg_and_fru;

SELECT name AS "Фрукт", calorie AS "MIN калории"
FROM veg_and_fru
WHERE type = 'Фрукт'
ORDER BY calorie  ASC
LIMIT 1;

SELECT name AS "Фрукт", calorie AS "MAX калории"
FROM veg_and_fru
WHERE type = 'Фрукт'
ORDER BY calorie DESC
LIMIT 1;