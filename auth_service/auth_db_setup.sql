-- Создаем базу данных auth_service
CREATE DATABASE auth_service;

-- Подключаемся к базе данных auth_service
\c auth_service;

-- Создаем пользователя с паролем
CREATE USER auth_user WITH PASSWORD 'secure_password';

-- Предоставляем пользователю права на управление базой данных auth_service
GRANT ALL PRIVILEGES ON DATABASE auth_service TO auth_user;

-- Убедитесь, что схема public существует
CREATE SCHEMA IF NOT EXISTS public;

-- Предоставляем пользователю доступ к схеме public
GRANT USAGE ON SCHEMA public TO auth_user;
GRANT CREATE ON SCHEMA public TO auth_user;

-- Назначаем права на создание, изменение и удаление таблиц
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO auth_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO auth_user;

-- Обеспечиваем управление будущими объектами в схеме public
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO auth_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON SEQUENCES TO auth_user;
