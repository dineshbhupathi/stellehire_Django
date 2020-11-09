Technology Stack:
Python 3.8.6
Django==3.1.3

clone project using this url:
git clone https://github.com/dineshbhupathi/stellehire_Django.git

To run project install requirements with below command
pip install -r requirements.txt

apply migrations to database below commands:
python manage.py makemigrations
python manage.py migrate

Now you have to load the data with json file which means feeding data into database with below command

python manage.py loaddata fixtures/usercreation.json

then run project:(command)
python manage.py runserver