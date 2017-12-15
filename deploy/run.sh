#!/bin/bash

APP=/app


cd $APP
while [ $n -lt 5 ]
do
    python manage.py run server
    break
done
