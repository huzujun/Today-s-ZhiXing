rm app.db
rm -r migrations
python3 migrate.py db init
python3 migrate.py db migrate
python3 migrate.py db upgrade
rm -rf project/static/*
cp project/resources/copy.ini project/resources/config.ini