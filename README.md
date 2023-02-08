# Repositorio oficial del curso: [Django Avanzado: Funciones extra e integraciones](https://netzun.com/cursos-online/django-avanzado-funciones-extra-integraciones?utm=carloalva)

## Descripción
El código fuente de este repositorio es el resultado de los ejemplos vistos en el curso.
***Para el despliegue en amazon se usa la rama "aws_deploy"***.

## Instalación de dependencias con pipenv
``` bash
pipenv install --dev
pipenv shell
```

## Instalación de dependencias con pip
``` bash
venv env
source env/bin/activate
pip install -r requirements.txt
```

## Levantar proyecto
``` bash
python manage.py runserver 0.0.0.0:8000
```

# Start project using heroku
``` bash
heroku login
heroku create
heroku local web --port 5001
git push heroku main
```
