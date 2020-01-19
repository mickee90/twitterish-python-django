# twitterish-python-django

1. cd into your project folder and enter `virtualenv twitterish`. This will create a new folder with files handling your virtual enviroment.

2. cd into the twitterish and `git clone https://github.com/mickee90/twitterish-python-django.git`

3. Enter `source bin/activate` to start the enviroment

4. Enter `pip install django` to install django in the enviroment

5. Enter `python manage.py migrate` to create the database

6. Enter `python manage.py createsuperuser` and fill the username, email and password

7. Finally enter `python manage.py runserve` to start the server. Go to the url, register a user and start tweeting!
