#!/bin/bash
source venv/bin/activate

echo "# -------------------"
echo "# running nosetests"
echo "# -------------------"
nosetests --with-coverage --cover-erase --cover-inclusive --cover-package=app

echo "# -------------------"
echo "# pyflakes"
echo "# -------------------"
pyflakes app/ tests/

echo "# -------------------"
echo "# black"
echo "# -------------------"
black -l 120
