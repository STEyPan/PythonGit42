ALTER TABLE clients
ADD COLUMN price numeric CHECK (price > 0);

SELECT * FROM clients;

ALTER TABLE programmers
ADD COLUMN salary numeric CHECK (salary > 0);

SELECT * FROM programmers;

ALTER TABLE project_manager
ADD COLUMN salary numeric CHECK (salary > 0);

SELECT * FROM project_manager;