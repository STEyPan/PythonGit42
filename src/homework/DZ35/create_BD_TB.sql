-- DROP TABLE "Faculties", "Departaments";

-- CREATE TABLE "Departaments" (
-- 	id uuid NOT NULL DEFAULT gen_random_uuid(),
-- 	financing numeric NOT NULL DEFAULT(0) CHECK (Financing >= 0),
-- 	name text NOT NULL UNIQUE CHECK (name <> ''),
-- 	PRIMARY KEY (id)
-- )

-- CREATE TABLE "Faculties" (
-- 	id uuid NOT NULL DEFAULT gen_random_uuid(),
-- 	dean text NOT NULL CHECK (dean <> ''),
-- 	name text UNIQUE NOT NULL CHECK (name <> ''),
-- 	PRIMARY KEY (id)
-- )

-- CREATE TABLE "Groups" (
-- 	id uuid NOT NULL DEFAULT gen_random_uuid(),
-- 	name text UNIQUE NOT NULL CHECK (name <> ''),
-- 	rating int NOT NULL CHECK (rating >= 0 AND rating <=5),
-- 	year int NOT NULL CHECK (year > 0 AND year <= 5),
-- 	PRIMARY KEY (id)
-- )

