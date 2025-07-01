-- DROP TABLE "Faculties";

-- CREATE TABLE "Departaments" (
-- 	id uuid NOT NULL DEFAULT gen_random_uuid(),
-- 	financing numeric NOT NULL DEFAULT(0) CHECK (Financing >= 0),
-- 	name varchar(100) NOT NULL UNIQUE CHECK (name <> ''),
-- 	PRIMARY KEY (id)
-- )

-- CREATE TABLE "Faculties" (
-- 	id uuid NOT NULL DEFAULT gen_random_uuid(),
-- 	dean varchar(255) NOT NULL CHECK (dean <> ''),
-- 	name varchar(100) UNIQUE NOT NULL CHECK (name <> ''),
-- 	PRIMARY KEY (id)
-- )