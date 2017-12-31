# StewPolley Django Example

This repository is designed as a tool to help teach people how to deploy
a Django app to an Ubuntu server, running NGINX and Gunicorn. This
repository by itself is not designed as a learning tool about Django in
a more general sense, although it could be expanded upon for various use
cases if you really wanted to.

Pull requests are welcome, especially if you want to actually make this
app do something (ie, a simply blog)

## Requirements
- A MySQL server (running locally, or otherwise accessible)
- Python 3.6+
- django 2+
- django-mysql
- gunicorn
- mysqlclient
- python-env

## Running this app.
Full instructions will be published in an upcoming blog post at
[https://stewpolley.com/](https://stewpolley.com/)

Quick instructions until such time:
- Copy `.env-example` to just `.env` and give it the respective values you need
- Create a [Virtual Env to run in](https://virtualenv.pypa.io/en/stable/userguide/)
- `pip install -r requirements.txt`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py runserver`