# Test TeamCore

## ✨ Descripción
Este proyecto es una prueba de desarrollo para TeamCore.

<br />

## ✨ Crear `.env` usando este archivo de ejemplo `env.sample`

El significado de algunas variables se puede encontrar a continuación: 

- `DEBUG`: si es `True` la aplicación se ejecuta en modo de desarrollo.
    - Para el valor de producción, se debe usar `False`
- `SECRET_KEY`: clave secreta para la aplicación. 
    - Para el valor de producción, se debe usar una clave secreta aleatoria.
- `DJANGO_SETTINGS_MODULE`: nombre del módulo de configuración de Django.

<br />

## ✨ Cómo usarlo

> Descarga el código

```bash
$ git clone git@github.com:RobertArzolaC/test-team-core.git
$ cd test-team-core
```

<br />

### 👉 Instalando dependencias en el sistema operativo

> Instalar módulos a través de `VENV`  

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

<br />

> `Configurar base de datos`

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> `Cargar datos de prueba`

```bash
$ python manage.py loaddata apps/core/fixtures/backup.json
```

<br />

> `Iniciar la aplicación`

```bash
$ python manage.py runserver
```

En este punto, la aplicación se ejecuta en `http://127.0.0.1:8000/`

<br />

## ✨ TO-DO

- [ ] Agregar Celery para manejar las tareas asíncronas
- [ ] Configurar Redis como broker
- [ ] Agregar Flower para monitorear las tareas asíncronas
- [ ] Agregar Docker para el despliegue

<br />

## ✨ Estructura base del código

El proyecto está codificado utilizando una estructura simple e intuitiva que se presenta a continuación:

```bash
< PROJECT ROOT >
   |
   |-- config/                          # Implements app configuration
   |    |-- settings.py                 # Defines Global Settings
   |    |-- urls.py                     # Define URLs served by all apps/
   |    |-- wsgi.py                     # WSGI config for production
   |
   |-- apps/
   |    |
   |    |-- core/                       
   |    |    |-- views.py               # Handles
   |    |    |-- urls.py                # Define routes
   |    |    |-- models.py              # Define models  
   |    |
   |    |-- home/             
   |    |    |-- urls.py                # Define routes  
   |    |    |-- views.py               # Handles
   |    |    |-- models.py              # Define models
   |    |
   |    |-- exchange/             
   |    |    |-- urls.py                # Define routes  
   |    |    |-- views.py               # Handles  
   |    |    |-- models.py              # Define models
   |    
   |-- templates/                       # Templates used to render pages
   |    |-- layouts/                    # Master pages
   |    |    |-- base.html              # Used by common pages
   |    |
   |    |-- home/                       
   |         |-- index.html             # Index page
   |
   |-- requirements.txt                 # Development modules
   |-- manage.py                        # Start the app - Django default start script
   |-- .env                             # Inject Configuration via Environment
   |
   |-- ************************************************************************
```
