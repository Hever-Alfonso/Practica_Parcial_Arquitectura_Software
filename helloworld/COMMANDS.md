# Comandos Técnicos – Proyecto Django Dockerizado

---

## 🐳 Docker

### Construir y levantar proyecto
```bash
docker compose up --build
```

### Ejecutar en segundo plano
```bash
docker compose up -d
```

### Detener contenedores
```bash
docker compose down
```

### Detener y eliminar volumen (BORRA BD)
```bash
docker compose down -v
```

### Ver logs
```bash
docker compose logs -f
```

---

## 🛠 Comandos dentro del contenedor

### Aplicar migraciones
```bash
docker compose exec web python manage.py migrate
```

### Crear superusuario
```bash
docker compose exec web python manage.py createsuperuser
```

### Crear migraciones
```bash
docker compose exec web python manage.py makemigrations
```

### Abrir shell Django
```bash
docker compose exec web python manage.py shell
```

### Entrar al contenedor
```bash
docker compose exec web bash
```

---

## 💻 Ejecución Local (sin Docker)

### Activar entorno virtual (Windows)
```bash
venv\Scripts\activate
```

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Ejecutar servidor
```bash
python helloworld/manage.py runserver
```

---

## 📌 URLs importantes

Aplicación:
```
http://localhost:8000
```

Admin:
```
http://localhost:8000/admin
```