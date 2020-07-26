# Suri
Suri is a Django app made for enabling STEM students to cooperate.
Students are able to pose questions, answer them and review answers.

### Installation
- Get the latest version of Python at https://www.python.org/downloads/
or with your operating system’s package manager.
- Install `pip` (download [get-pip.py](https://bootstrap.pypa.io/get-pip.py)
and run the following command in the same folder: `python get-pip.py`)
- (optional) Create and activate a new
[virtual environment](https://docs.python.org/3/tutorial/venv.html)
- Run the following commands:
```
pip install Django
pip install django-notifications-hq
pip install django-bootstrap-modal-forms
```

### Starting the server
Inside Suri folder run the following commands:
```
python manage.py migrate
python manage.py runserver
```
Visit http://localhost:8000/ with your Web browser.
