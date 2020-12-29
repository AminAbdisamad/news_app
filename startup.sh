#!/bin/sh
pipenv shell
gunicorn -w 2 -b 0.0.0.0:8080 run:app