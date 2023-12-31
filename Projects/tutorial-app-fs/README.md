<!-- hocanin notlari -->
#Backend
# Full Stack Project Tutorial App- Backend

```
# KURULUM KOMUTLARI
   1 py -m venv env
   2 .\env\Scripts\activate
   3 pip install djangorestframework
   5 django-admin startproject main .
   6 pip install python-decouple
   7 py manage.py migrate
   8 py manage.py createsuperuser
   9 py manage.py startapp tutorial
```
## How To Use Repo

<!-- This is an example, please update according to your application -->

To clone and run this application, you'll need [Git](https://git-scm.com)

```Python

# Clone this repository
$ git clone https://github.com/your-user-name/your-project-name

# Install dependencies
    $ cd api
    $ python -m venv env
    > env/Scripts/activate (for win OS)
    > source env/Scripts/activate(for bash)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt

# Edit .backend.env to .env

# Add SECRET_KEY in .env file
# migrate
    $ python manage.py migrate
# Run the app
    $ python manage.py runserver
```

<li>Frontend kısmını apimize bağlayabilmek için cors-headers paketini kullanacağız</li>
<a href="https://github.com/adamchainz/django-cors-headers">Cors Headers paketi için</a>

# Frontend
# API Base URLs

## http://127.0.0.1:8000/tutorials/


### API ENDPOINTS

- GET `api/tutorials/` get all Tutorials
- GET `api/tutorials/:id/` get Tutorial by id
- POST `api/tutorials/` add new Tutorial
- PUT `api/tutorials/:id/` update Tutorial by id
- DELETE `api/tutorials/:id/` remove Tutorial by id
- DELETE `api/tutorials/` remove all Tutorials

## How To Use Repo

<!-- This is an example, please update according to your application -->

To clone and run this application, you'll need [Git](https://git-scm.com)

```JavaScript

// Clone this repository
$ git clone https://github.com/your-user-name/your-project-name

// Install dependencies
    $ cd client
    $ npm or yarn install
// Run the app
    $ npm or yarn start
```


<!-- benim notlarim 
- search django corsheaders
- https://pypi.org/project/django-cors-headers/
- pip install django-cors-headers      or      python -m pip install django-cors-headers

- INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
]

- MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...,
]                                       -> that means add the line (CorsMiddleware) oben the CommonMiddleware

- CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]

or

- CORS_ALLOW_ALL_ORIGINS=True

- CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)




 -->
