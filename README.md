## What is this repository for? ##

Various web apps for various events which will take place during felicity buzz2k15.

## How do I get set up? ##

**Install the requirements:**

1. virtualenv --no-site-packages --distribute venv
2. source venv/bin/activate
3. pip install -r requirements.txt

**Entering the virtual environment**

1. source venv/bin/activate

**Create/Sync the database:**

1. ./manage.py makemigrations 
2. ./manage.py migrate

**Starting the server:**

1. ./manage.py runserver [host:port]

**Exiting the virtual environment**

1. deactivate

##Important##
As it is better to serve static files with nginx, I made a bypass uwsgi system to server static pages like home,events,scedule page so please use /Felicity-buzz2k15/staticpages/ for this type of pages.

Use /Felicity-buzz2k15/buzz2k15/ folder for django related work

Site link -> felicity.iiit.ac.in/buzz/ (accessible only through intranet)

If you  provide any link  use /buzz/portal/ as prefix
