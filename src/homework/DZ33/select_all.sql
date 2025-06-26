SELECT * 
FROM veg_and_fru
WHERE type = 'Фрукт';

SELECT name
FROM veg_and_fru;

SELECT DISTINCT color
FROM veg_and_fru;

SELECT *
FROM veg_and_fru
WHERE type = 'Фрукт' AND color = 'Желтый';

SELECT *
FROM veg_and_fru
WHERE type = 'Овощ' AND color = 'Зеленый'