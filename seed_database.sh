rm db.sqlite3
rm -rf ./responsiblyapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations responsiblyapi
python3 manage.py migrate responsiblyapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata clients
python3 manage.py loaddata shops
python3 manage.py loaddata todos

# python3 manage.py loaddata attractionTypes
# python3 manage.py loaddata attractions
# python3 manage.py loaddata restaurants
# python3 manage.py loaddata murals
# python3 manage.py loaddata savedMurals

# Run this command to seed database:    chmod u+x ./seed_database.sh