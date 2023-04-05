# python app starter ![example workflow](https://github.com/leafwind/create-python-app/actions/workflows/main.yml/badge.svg)

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

# Building package of your app

This repo includes a `setup.py` script for others to install your app by Github URL.

# How to use the built package?

## Option1: Write into `requirements.txt`

1. Add this line in your `requirements.txt`:
  - `git+ssh://github.com/leafwind/create-python-app.git@[tag_name]#egg=create-python-app`
2. `pip install -r requirements.txt`

## Option2: install via pip

1. `pip install ssh://github.com/leafwind/create-python-app.git@[tag_name]#egg=create-python-app`
2. Uninstall
  - `pip uninstall create-python-app`

---

## Docker usage

### build

`docker_build.sh`

### run

`docker_run.sh`

---

## run check script before commit

`./scripts/pre_commit_check.sh`

check https://pre-commit.com/ to setup pre-commit hook.

