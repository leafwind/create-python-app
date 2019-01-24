#!/bin/bash

echo build python virtualenv on $1 from $2

cd $1
virtualenv venv --no-site-packages
. venv/bin/activate
pip install --upgrade pip
pip install -r $2
deactivate
