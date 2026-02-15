# =========================================================
# Dockerfile
# Proyecto Django - Arquitectura de Software
# =========================================================

# Imagen base oficial de Python
FROM python:3.12-slim

# Evita archivos .pyc y fuerza salida inmediata en logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos requirements primero (mejor para cache)
COPY requirements.txt /app/

# Instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el proyecto
COPY . /app/

# Exponemos puerto de Django
EXPOSE 8000

# Comando para ejecutar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
