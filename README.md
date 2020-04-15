# Minerals World
## Description
A mineral catalog web application. The main (index) page lists minerals' name. Each mineral name links to a detail page that displays image, category, formula and other related information.

## Screenshot
index page
<<img src="https://raw.githubusercontent.com/yushinna/python-project-06/images/index-page.png" width="600">

detail page
<<img src="https://raw.githubusercontent.com/yushinna/python-project-06/images/detail-page.png" width="600">

## Requirements
Install the project requirements from the provided Pipfile by running the following command in your terminal:
```
pipenv install
```

## Usage
Run server by Django, enter given url (`http://127.0.0.1:8000` by default) on browser so you can interact with the app!

```
# enter virtual environment
pipenv shell

# create database and load data from json file
python manage.py migrate

#run Django app
python manage.py runserver
```
