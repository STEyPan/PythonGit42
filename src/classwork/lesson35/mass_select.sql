SELECT clients.name as client, 
	   projects.title as project, 
	   project_manager.name as pm,
	   tasks.description as task,
	   programmers.name as prog,
	   programmers.telephone as contact
	   
FROM clients, projects, project_manager, tasks, programmers, task_programmers

WHERE clients.client_id = projects.client_id 
	  AND projects.project_manager_id = project_manager.manager_id
	  --AND projects.title = 'Создание мобильного приложения'
	  AND tasks.project_id = projects.project_id
	  AND task_programmers.prog_id = programmers.prog_id
	  AND task_programmers.task_id = tasks.task_id;


-- SELECT clients.client_id as client, 
-- 	   projects.project_id as project, 
-- 	   project_manager.manager_id as pm
	   
-- FROM clients, projects, project_manager

-- WHERE clients.client_id = projects.client_id 
-- 	  AND projects.project_manager_id = project_manager.manager_id;