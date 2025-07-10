-- DROP TABLE "Faculties", "Departaments";
-- DROP TABLE teacher;

CREATE TABLE departaments (
	id uuid NOT NULL DEFAULT gen_random_uuid(),
	financing numeric NOT NULL DEFAULT(0) CHECK (Financing >= 0),
	name text NOT NULL UNIQUE CHECK (name <> ''),
	PRIMARY KEY (id)
);

CREATE TABLE faculties (
	id uuid NOT NULL DEFAULT gen_random_uuid(),
	dean text NOT NULL CHECK (dean <> ''),
	name text UNIQUE NOT NULL CHECK (name <> ''),
	PRIMARY KEY (id)
);

CREATE TABLE groups (
	id uuid NOT NULL DEFAULT gen_random_uuid(),
	name text UNIQUE NOT NULL CHECK (name <> ''),
	rating int NOT NULL CHECK (rating >= 0 AND rating <=5),
	year int NOT NULL CHECK (year > 0 AND year <= 5),
	PRIMARY KEY (id)
);

CREATE TABLE teacher (
	id uuid NOT NULL DEFAULT gen_random_uuid(),
	employment_date date NOT NULL CHECK (employment_date > '01.01.1990'),
	is_assistant boolean NOT NULL DEFAULT False,
	is_professor boolean NOT NULL DEFAULT False,
	name text NOT NULL CHECK (name <> ''),
	surname text NOT NULL CHECK (surname <> ''),
	position text NOT NULL CHECK (position <> ''),
	premium numeric NOT NULL DEFAULT (0) CHECK (premium >= 0),
	salary numeric NOT NULL CHECK (salary > 0),

	PRIMARY KEY (id)
);