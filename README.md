# Carsnepal

A car directory web application on `python3.8` and `Django4.0`.

## Local development

To run this project in your development machine, follow these steps:

1. (optional) Create and activate a [virtualenv](https://virtualenv.pypa.io/) (you may want to use [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/)).

2. Fork this repo and clone your fork:

    `git clone https://github.com/surajbhattrai/carsnepal/`

3. Install dependencies:

    `pip install -r requirements.txt`

4. Create a development database:

    `./manage.py migrate`

5. If everything is alright, you should be able to start the Django development server:

    `./manage.py runserver`

6. Open your browser and go to http://127.0.0.1:8000, you will be greeted with a welcome page.
