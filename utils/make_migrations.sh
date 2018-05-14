#!/bin/bash
#

python3 ../apps/manage.py makemigrations

python3 ../apps/manage.py makemigrations users

python3 ../apps/manage.py makemigrations navis

python3 ../apps/manage.py makemigrations perms

python3 ../apps/manage.py makemigrations common

python3 ../apps/manage.py makemigrations projects

python3 ../apps/manage.py migrate

