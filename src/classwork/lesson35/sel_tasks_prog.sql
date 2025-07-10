SELECT 
	tasks.project_id, tasks.description,
	programmers.name, programmers.telephone

FROM
	task_programmers
	
LEFT JOIN tasks ON task_programmers.task_id = tasks.task_id
RIGHT JOIN programmers ON task_programmers.prog_id = programmers.prog_id;