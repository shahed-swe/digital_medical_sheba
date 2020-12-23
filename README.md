# Digital Sheba Project
 

## Building

It is best to use the python `virtualenv` tool to build locally:

```sh
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ DEVELOPMENT=1 python manage.py runserver
```

Then visit `http://localhost:8000` to view the app. Alternatively you
can use foreman and gunicorn to run the server locally (after copying
`dev.env` to `.env`):


## Deploy to Heroku

Run the following commands to deploy the app to Heroku:

```sh
$ git clone https://github.com/shahed-swe/digital_medical_sheba.git
$ cd examples-django
$ heroku create
$ heroku addons:add memcachier:dev
$ git push heroku master:master
$ heroku open
```

## requirements.txt


Don't forget to update your requirements.txt file with these new pips.
requirements.txt should have the following two lines:

```
asgiref==3.2.10
Django==3.1.2
django-cors-headers==3.5.0
django-rest-framework==0.1.0
djangorestframework==3.12.1
requests
gunicorn==20.0.4
```
## Let's See how to run
```
python manage.py runserver
```
