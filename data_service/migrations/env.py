from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from app.models import Base  
from app.database import engine  

# Настройки Alembic
config = context.config
fileConfig(config.config_file_name)

# Подключаем метаданные моделей
target_metadata = Base.metadata

def run_migrations_offline():
    """Миграция в оффлайн-режиме."""
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Миграция в онлайн-режиме."""
    connectable = engine

    with connectable.connect() as connection:
        # Настраиваем миграции без попытки пересоздать существующие таблицы
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # Для учета различий в типах столбцов
            compare_server_default=True,  # Для учета значений по умолчанию
            version_table="alembic_version_data_service",  # Отдельная таблица версий для Data Service
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
