# feedex

## Installation

To run this program, first create and activate a virtual enviroment within the `src/` folder

```
$ python3 -m pip install virtualenv venv
$ . venv/bin/activate
```

Then run to install dependencies
```
(venv) $ pip install -r requirements.txt
```

You can run the project with
```
(venv) $ python3 manage.py runserver
```

You can update the database schema with
```
(venv) $ python3 manage.py makemigrations
(venv) $ python3 manage.py migrate
```