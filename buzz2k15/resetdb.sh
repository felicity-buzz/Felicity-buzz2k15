rm db.sqlite3
rm home/migrations/00*
rm home/migrations/*.pyc
rm authentication/migrations/00*
rm authentication/migrations/*.pyc
python manage.py makemigrations
python manage.py migrate

