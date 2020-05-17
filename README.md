# python app starter [![Build Status](https://travis-ci.org/leafwind/create-python-app.svg?branch=master)](https://travis-ci.org/leafwind/create-python-app) [![Coverage Status](https://coveralls.io/repos/github/leafwind/create-python-app/badge.svg?branch=master)](https://coveralls.io/github/leafwind/create-python-app?branch=master)

a dog food template repository for myself

## Features

- main with arguments
- logging format
- `Dockerfile` and shell script to make docker image
- `setup.py` to make package


## main.py

contains basic arguments and logging function

### Logging Format

[Tip: Use a Human-Readable Logging Format](https://reflectoring.io/logging-format/)
- Highly human readable
  - clearly distinguish the different information blocks at a glance
  - know in which column to look for the information we’re currently searching
- Which Information to Include
  - Date & Time
  - Logging level
  - Logger name
  - File name
  - Line number
  - The message itself
- An example
```
> python app/main.py 
[INFO] 2020-02-28 21:40:04 | root |              main.py |  43 | dry run: True
```

## build virtualenv first

`./scripts/build_venv.sh`

## run check script before commit

`./scripts/pre_commit_check.sh`
