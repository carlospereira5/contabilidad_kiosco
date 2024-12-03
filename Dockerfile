FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Establece el directorio de trabajo
WORKDIR /app

# Configura variables de entorno
ENV PYTHONPATH "${PYTHONPATH}:/"
ENV PORT=8000

# Actualiza pip
RUN pip install --upgrade pip

# Copia las dependencias del proyecto
COPY ./requirements.txt /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia los archivos de configuración y del proyecto
COPY ./app /app
COPY ./alembic /app/alembic
COPY ./alembic.ini /app/alembic.ini

