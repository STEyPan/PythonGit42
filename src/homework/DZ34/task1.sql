SELECT *
FROM veg_and_fru
WHERE type = 'Овощ' AND calorie > 20;

SELECT *
FROM veg_and_fru
WHERE type = 'Фрукт' AND calorie > 30;

SELECT *
FROM veg_and_fru
WHERE type = 'Овощ' AND name ILIKE '%перец%';

SELECT *
FROM veg_and_fru
WHERE description ILIKE '%сахар%';

SELECT *
FROM veg_and_fru
WHERE color ILIKE '%красный%' OR color ILIKE '%желтый%';

SELECT *
FROM veg_and_fru
WHERE color IN ('Красный','Желтый');