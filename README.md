# Portfolio API

This is a Django-based API for managing a portfolio with blogs and projects.

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables:
   - DJANGO_SECRET_KEY
   - DJANGO_DEBUG
4. Run migrations: `python manage.py migrate`
5. Create a superuser: `python manage.py createsuperuser`
6. Run the server: `python manage.py runserver`

## Deployment

This application is ready to be deployed to Heroku or similar platforms.

1. Create a new Heroku app
2. Set the environment variables in Heroku's settings
3. Deploy the code to Heroku
4. Run migrations on Heroku: `heroku run python manage.py migrate`
5. Create a superuser on Heroku: `heroku run python manage.py createsuperuser`

## API Documentation

API documentation is available at the `/swagger/` endpoint when the server is running.