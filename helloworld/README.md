# Práctica Parcial – Arquitectura de Software
## Proyecto Django Dockerizado

---

## 📌 Descripción del Proyecto

Este proyecto corresponde a la práctica parcial del curso de **Arquitectura de Software**.

La aplicación fue desarrollada utilizando el framework **Django**, aplicando el patrón de arquitectura **MVT (Model – View – Template)**.

El proyecto se encuentra completamente **dockerizado**, lo que permite:

- Reproducibilidad del entorno
- Portabilidad
- Aislamiento de dependencias
- Persistencia de datos
- Facilidad de despliegue

---

## 🏗 Arquitectura del Sistema

El proyecto implementa el patrón **MVT** propio de Django.

### 📂 Estructura General

```
.
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
├── README.md
└── helloworld/
    ├── manage.py
    ├── data/
    ├── helloworld_project/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    └── pages/
```

### 🔎 Componentes Principales

- **Models** → Definen la estructura de la base de datos.
- **Views** → Controlan la lógica del negocio.
- **Templates** → Manejan la presentación.
- **Docker** → Conteneriza la aplicación.
- **Docker Compose** → Orquesta los servicios.

---

## 🐳 Ejecución con Docker (Recomendado)

### 🔹 1. Construir y levantar el proyecto

```bash
docker compose up --build
```

Esto construye la imagen y levanta el contenedor.

Abrir en el navegador:

```
http://localhost:8000
```

---

### 🔹 2. Aplicar migraciones

En otra terminal:

```bash
docker compose exec web python manage.py migrate
```

---

### 🔹 3. Crear superusuario (opcional)

```bash
docker compose exec web python manage.py createsuperuser
```

Panel admin:

```
http://localhost:8000/admin
```

---

### 🔹 4. Detener contenedores

```bash
docker compose down
```

---

### 🔹 5. Eliminar volumen (BORRA la base de datos)

```bash
docker compose down -v
```

---

## 💻 Ejecución en Local (Sin Docker)

### 1️⃣ Crear entorno virtual

```bash
python -m venv venv
```

Activar entorno:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

---

### 2️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Aplicar migraciones

```bash
python helloworld/manage.py migrate
```

---

### 4️⃣ Ejecutar servidor

```bash
python helloworld/manage.py runserver
```

Abrir:

```
http://127.0.0.1:8000
```

---

## 💾 Persistencia de Datos

La base de datos SQLite se almacena en un volumen Docker:

```
sqlite_data
```

La configuración en `settings.py` apunta a:

```
helloworld/data/db.sqlite3
```

Esto permite que los datos no se pierdan al reiniciar el contenedor.

---

## 🔐 Buenas Prácticas Implementadas

- Uso de `.gitignore` para evitar subir archivos innecesarios
- Separación clara de responsabilidades (MVT)
- Dockerización del entorno
- Uso de volumen para persistencia de datos
- Documentación estructurada

---

## 📚 Tecnologías Utilizadas

- Python 3.12
- Django 3.2.12
- Docker
- Docker Compose
- SQLite

---

## 👨‍💻 Autor

**Hever Alfonso**  
Universidad EAFIT  
Curso: Arquitectura de Software  
Año: 2026