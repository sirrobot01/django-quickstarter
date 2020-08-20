# Django-Quickstarter

[![Updates](https://pyup.io/repos/github/sirrobot01/django-quickstarter/shield.svg)](https://pyup.io/repos/github/sirrobot01/django-quickstarter/)
[![Python 3](https://pyup.io/repos/github/sirrobot01/django-quickstarter/python-3-shield.svg)](https://pyup.io/repos/github/sirrobot01/django-quickstarter/)

## What's included

- Custom user
- Authentication(JWT) with Registration
- Requirements file
- Django REST framework
- API Documentations(Swagger & Redoc)
- Django CORS headers

## Installation

Prepare a virtual environment in a folder of choice and install Django:

```bash
mkdir newproject && cd $_
python3 -m venv venv
source venv/bin/activate
pip install django
```

Then install the template:

```bash
django-admin startproject --template https://github.com/sirrobot01/django-quickstarter/archive/master.zip newproject .
```

Install the dependencies:

```bash
pip install -r requirements.txt
```


Before starting off make the migrations for the custom User and Authentications:

```bash
python manage.py makemigrations
python manage.py migrate
```

and you are good to go!!

### SSL Issues on MacOS

You might encounter an issue starting the project. You have two options

#### Option 1

- Clone this repo: 
```git clone https://github.com/sirrobot01/django-quickstarter.git ```
```bash
mkdir newproject && cd $_
python3 -m venv venv
source venv/bin/activate
pip install django
```

Then install the template:

```bash
django-admin startproject --template django-quickstarter newproject .
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

```bash
python manage.py makemigrations
python manage.py migrate
```




#### Option 2

- Click on "Use this template"
- Create a new repo off this on your account
- Pull/Clone to your local computer
- Create a virtualenv
- ```pip install -r requirements.txt```
```bash
python manage.py makemigrations
python manage.py migrate
```

## Endpoints

##### Authentications

- Register `POST` `/auth/register/`
- Login `POST` `/auth/login/`
- Refresh JWT Token `POST` `/auth/refresh/`
- Verify JWT Token `POST` `/auth/verify/`

```
Note: Check /swagger/ or /redoc/ for other endpoints
```

##### Documentations

- Swagger `GET` `/swagger`
- Redoc `GET` `/redoc/`

## Running Tests

```bash
python manage.py test
```
