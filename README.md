# EETC Data Client


## System requirements
To run the project locally and work on it, you need the following:
- Python 3.8+

## Project setup
```commandline
sudo apt-get install build-essential
make update_and_install_python_requirements
```

## Adding a new Python package
1. Add the package name to `requirements.in`
2. Run:
```commandline
make update_and_install_python_requirements
```
