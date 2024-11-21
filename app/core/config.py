from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

# Determinar el archivo de entorno a utilizar
env_file = ".env.local" if os.path.exists(".env.local") else ".env"

class Settings(BaseSettings):
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: Union[str, List[AnyHttpUrl]] = []

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    def assemble_cors_origins(cls, v):
        if isinstance(v, str):
            # Remover corchetes y comillas, luego dividir por comas
            v = v.strip('"\'[]')
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, list):
            return v
        else:
            raise ValueError("Invalid value for BACKEND_CORS_ORIGINS")

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_URI: Optional[str] = None

    @field_validator("DATABASE_URI", mode="before")
    def assemble_db_connection(cls, v, info):
        if v is not None:
            return v
        data = info.data
        user = data["POSTGRES_USER"]
        password = data["POSTGRES_PASSWORD"]
        server = data["POSTGRES_SERVER"]
        db = data["POSTGRES_DB"]
        return f"postgresql://{user}:{password}@{server}/{db}"

    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=env_file,
    )

settings = Settings()

# Añadir impresiones para verificar los valores cargados
print(f"Using env_file: {env_file}")
print(f"POSTGRES_SERVER: {settings.POSTGRES_SERVER}")
print(f"DATABASE_URI: {settings.DATABASE_URI}")
