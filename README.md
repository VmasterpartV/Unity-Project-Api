# **Unity-Project-Api** #

## Descripción ##

Back y apis consumibles del proyecto

## Features

- Django 3.0+
- [Django REST Framework](https://www.django-rest-framework.org/) - Powerful and flexible toolkit for building Web APIs.
- [Django Cors Headers](https://pypi.org/project/django-cors-headers/) - A Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS).
- [Django Filter](https://django-filter.readthedocs.io/en/stable/) - Simple way to filter down a queryset based on parameters a user provides.
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - A JSON Web Token authentication plugin for the Django REST Framework.
- Procfile for running gunicorn with New Relic's Python agent.
- Support for automatic generation of [OpenAPI](https://www.openapis.org/) schemas.
- Automated generation of real Swagger/OpenAPI 2.0 schemas from Django REST Framework code with [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/).

## Prerequisites

- Python 3.7>
- Virtualenv
## Instalation

    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt

### DEV

Just make a copy from `.env.local.example` and/or rename to `.env.local` and setup your variables. Then run in terminal:

    $ source .env.local

The first time you run the application, make sure to apply the database migrations and create a super user account:

    $ python manage.py migrate
    $ python manage.py createsuperuser

Finally start development server:

    $ python manage.py runserver

### Update Dependencies
    
    $ pip freeze > requirements.txt
