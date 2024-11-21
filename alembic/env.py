import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Importar la configuración y los modelos de tu aplicación
from app.core.config import settings
from app.database import Base

# Obtener la configuración de Alembic
config = context.config

# Configurar la URL de la base de datos desde tus settings
config.set_main_option('sqlalchemy.url', settings.DATABASE_URI)

# Interpretar el archivo de configuración de logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Establecer el target_metadata para 'autogenerate'
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Ejecuta las migraciones en modo 'offline'.

    Esto configura el contexto solo con una URL y no un Engine.
    Las llamadas a context.execute() aquí emiten el string dado en la salida del script.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Ejecuta las migraciones en modo 'online'.

    En este escenario, necesitamos crear un Engine y asociar una conexión con el contexto.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
