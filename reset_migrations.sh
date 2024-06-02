#! /usr/bin/bash
cd ./PlywoodTickets;

rm -r ./mainpage/__pycache__;
rm -r ./mainpage/migrations;

rm -r ./personalLocker/__pycache__;
rm -r ./personalLocker/migrations;

rm -r ./PlywoodTickets/__pycache__;

python manage.py makemigrations mainpage;
python manage.py makemigrations personalLocker;
python manage.py migrate;
echo "Finished";