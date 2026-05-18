# Sistema de Gestión Académica - UPLA 2026-I

Proyecto desarrollado con Scrum usando Django 5.1 y GitHub Projects.

## Tecnologías

- Python 3.13
- Django 5.1
- Django REST Framework
- SQLite3
- Git y GitHub

## Integrantes

- Josue Nehemias
- Elias Matos
- Roy Tornero Rojas
- Integrante 4

## Instalación

```bash
git clone https://github.com/eliasmatos1956/sga-TeamFour.git
cd sga-TeamFour

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
