# **Art-Project-Api** #

## Descripción ##

Back y apis consumibles del proyecto

## Requisitos previos ##
- [Python](https://www.python.org/downloads/)
- [VSCode](https://visualstudio.microsoft.com/es/downloads/)
- [Github](https://desktop.github.com/)
- [Git](https://git-scm.com/downloads)
- [POSTMAN](https://www.postman.com/downloads/)

## Comandos de instalación ##

    `pip install`

## Comandos ejecución ##

    `virtualenv venv --python=python`
    
    `.\venv\Scripts\activate`

    `python manage.py runserver`
    
    `python manage.py help`

    ### *Aplicar cambios de modelos* ###

    `python manage.py makemigrations`

### *Migrar cambios de modelos* ###

    `python manage.py migrate` 

### *Crear un superusuario* ###

    `python manage.py createsuperuser`

## Comandos adicionales ##

### *Actualizar dependencias cada que se instale una nueva libreria* ###
    
    `pip freeze > requirements.txt`

    `pip install -r requirements.txt`

    `pip freeze`

### *Crear archivo settings local.py*###

# **_Github y Git_** #

### *Crear repositorio nuevo* ###
  
    `git init`

### *Add and commit git add (nombre de archivo)* ###

    `git commit -m "commit"`

### *Envio de cambios* ###
    
    `git push origin` (rama en la cual vas a enviar cambios)

### *Crear y cambiar de rama* ###
    
    `git checkout -b (nombre de rama)`

### *Volver a rama principal* ###
    
    `git checkout master`

### *Borrar la rama* ###
    
    `git branch -d feature_x`

### *Hacer disponible a todos la rama (push)* ###
    
    `git push origin <nombre de rama>`

### *Actualizar repositorio local al commit mas nuevo* ###
    
    `git pull`

### *Fusionar rama con la que estas trabajando* ###
    
    `git merge <nombre de la rama>`