# feedex

## Installation

To run this program, first compile CSS files with gulp.

These are located in `src/frontend/static/assets/`

Run the following commands once at the directory
```
$ npm install
$ gulp
```

Then create and activate a virtual enviroment within the `src/` folder

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