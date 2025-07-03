-- Table Заказчики (name, contact, telephone)
--   <-
-- Table Проекты (заказчик, start, end, title)
--  <-
-- Table Tasks (проект, описание, начало, конец, ответ. лицо)
-- >-<
-- Table Программисты (ФИО, ДР, ур.навыков, telephone)
-- Проекты ->
-- Table Project_manager (ФИО, ДР, telephone)
-- Запрос (заказчик, проект, ProjMen, tasks proj, ФИО прог, телефон прог)


-- CREATE DATABASE "Projects";