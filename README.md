# Mecatrónica UNLZ

Blog de la carrera de Ingeniería Mecatrónica de la Universidad Nacional de Lomas de Zamora.

## Descripción

Plataforma donde los alumnos pueden compartir apuntes, parciales resueltos, clases particulares, noticias y proyectos.

## Tecnologías

- Python 3.13
- Django 6.0
- Bootstrap 5
- SQLite

## Instalación

1. Clonar el repositorio
```bash
git clone https://github.com/emmanuel18colab-cloud/mecatronica-unlz.git
cd mecatronica-unlz
```

2. Crear y activar el entorno virtual
```bash
python -m venv venv
venv\Scripts\activate
```

3. Instalar dependencias
```bash
pip install -r requirements.txt
```

4. Hacer las migraciones
```bash
python manage.py migrate
```

5. Crear superusuario
```bash
python manage.py createsuperuser
```

6. Correr el servidor
```bash
python manage.py runserver
```

## Funcionalidades

- Registro, login y logout de usuarios
- Perfil de usuario con avatar y biografía
- CRUD completo de posts
- Filtros por tipo, año y materia
- Mensajería entre usuarios
- Panel de administración