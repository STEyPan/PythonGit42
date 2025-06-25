--CREATE DATABASE Birds;

SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = 'birds' AND pid <> pg_backend_pid();

ALTER DATABASE "birds" RENAME TO "Cats";