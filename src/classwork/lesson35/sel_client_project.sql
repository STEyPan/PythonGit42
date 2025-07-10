SELECT 
	clients.client_id, clients.name,
	projects.project_id, projects.title

FROM 
	projects
	LEFT JOIN clients ON projects.client_id = clients.client_id;