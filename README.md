# Flow blog
## Overview
This is a simple and efficient blogging system, you can use it to publish their articles, each article must have a classification, which you should create, but the article can have multiple attributes of the label. At the same time, visitors can comment on the public article, of course, you can also reply to him.

You can create your own page, which will be shown on the home page, but unfortunately, when the page is too much time the home page will look very strange, but on this we will repair it later.

Blog supports multiple users to register and manage at the same time, but when the new user needs administrator authorization, the administrator can grant the user the appropriate administrative privileges, and the user can meet the permissions to grant it to others. In order to facilitate management, we introduced the concept of group, the group is equivalent to our authorized group of all users within the authorized.

***Created by qianqian***
## Development environment
`Python 3.5 + django 1.10`

## Features
- Simple and light
- Beautiful interface
- Practical django structures
- You can quickly build and configure


## Requirements
These dependencies are automatically installed:

    Django==1.10.4
    markdown==2.6.7
    Pillow==3.4.2
    bootstrap-admin==0.3.7.1
    PyMySQL==0.7.9
    pytz=2016.10

## Quick Start
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
Default site url: http://127.0.0.1:8000/ and sign in at http://127.0.0.1:8000/admin/ .

## Settings
**config file: flow/config/__init__.py**
### DBMS:Mysql

    DATABASE_CONFIG = {
        'NAME': 'pyblog',   #DB_NAME
        'USER': 'root',     #Mysql username
        'PASSWORD': 'im0qianqian',  #Mysql user_password
        'HOST': '127.0.0.1',    #Mysql host
        'PORT': '3306',     #Mysql service port
    }

### config

    MAXIMUM_OF_PAGE = 3
    SITE_URL = "http://localhost/"
    BLOG_TITLE = "FLOW BLOG"
    BLOG_DESCRIPTION = "Snow Memory"
    LOGO_IMAGE = "http://[An image].jpg"

