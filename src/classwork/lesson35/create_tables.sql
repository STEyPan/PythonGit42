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

-- DROP TABLE clients, programmers, projects, tasks, task_programmers, project_manager;

CREATE TABLE clients (
	client_id uuid NOT NULL DEFAULT gen_random_uuid(),
	name text NOT NULL,
	contact text,
	telephone text UNIQUE,

	PRIMARY KEY (client_id)
);

CREATE TABLE projects (
	project_id uuid NOT NULL DEFAULT gen_random_uuid(),
	title text NOT NULL,
	client_id uuid,
	start_project date NOT NULL,
	end_project date NOT NULL,
	CHECK (end_project > start_project),

	PRIMARY KEY (project_id),
	
	FOREIGN KEY (client_id) REFERENCES clients (client_id)
	ON UPDATE CASCADE
);

CREATE TABLE tasks (
	task_id uuid NOT NULL DEFAULT gen_random_uuid(),
	project_id uuid,
	description text,
	start_task date NOT NULL,
	end_task date NOT NULL,
	CHECK (end_task > start_task),

	PRIMARY KEY (task_id),
	
	FOREIGN KEY (project_id) REFERENCES projects (project_id)
	ON UPDATE CASCADE	
);

CREATE TABLE programmers (
	prog_id uuid NOT NULL DEFAULT gen_random_uuid(),
	name text NOT NULL,
	birthday date NOT NULL,
	skill text NOT NULL,
	telephone text UNIQUE,

	PRIMARY KEY (prog_id)
);

CREATE TABLE task_programmers (
	task_id uuid NOT NULL,
	prog_id uuid NOT NULL,
	
	PRIMARY KEY (task_id, prog_id),
	
	FOREIGN KEY (task_id) REFERENCES tasks (task_id)
	ON DELETE CASCADE  ON UPDATE CASCADE,
	
	FOREIGN KEY (prog_id) REFERENCES programmers (prog_id)
	ON DELETE CASCADE  ON UPDATE CASCADE
	
);

CREATE TABLE project_manager (
	manager_id uuid NOT NULL DEFAULT gen_random_uuid(),
	name text NOT NULL,
	telephone text UNIQUE,
	project_id uuid,

	PRIMARY KEY (manager_id),
	
	FOREIGN KEY (project_id) REFERENCES projects (project_id)
	ON UPDATE CASCADE
);