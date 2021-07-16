#!/bin/bash

# https://dev.to/lukeinthecloud/python-auto-reload-using-flask-ci6

set FLASK_APP=server.py
export FLASK_APP=server.py
export FLASK_ENV=development

flask run
