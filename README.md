# DjangoJsonUpload
Creating models from the uploaded data

Django User login,register and logout functionality added.
A model called Posts is present, which you can upload through a json file.

Clone the project, activate the virtual enviironment 'denvx'

.\denvx\scripts\activate for windows.
then 
pip install django
pip install django-crispy-forms

then run these commands:
python manage.py migrate
python manage.py makemigraions
python manage.py migrate

make sure to create a superuser before running the application.
existing superuser:
login - admin
password - admin
python manage.py createsuperuser

python manage.py runserver
