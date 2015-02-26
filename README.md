# resto
A restaurant app for fueled

## Dev Installation

Create a virtual env with virtualenv wrapper

    $ mkvirtualenv resto

Activate the environment:

    $ workon resto

Clone/Download this repo.

Install requirements by entering to the repo folder and run

    $ pip install -r requirements.txt

Initialize your local database:

    $ ./manage.py migrate

Create a superuser:

    $ ./manage.py createsuperuser

Enter username, email and password

Run a local test server:

    $ ./manage.py runserver

Visit the backend test landing page by opening your browser at localhost:8000


### Frontend App for testing:
In resto-ui folder you will find the frontend app to test the application.
To install it and run it you need to:

Enter to the folder:

    $ cd resto-ui

Install dependencies:

    $ npm install
    $ bower install

You might need to upgrade your compass gem. In that case run:

    $ sudo gem install compass --pre


Then run the app with grunt:

    $ grunt serve

Note: you need to have the Django App running on a different terminal to see the Front-end app working.

## Import Restaurants into the system
Factual.com is used to get the restaurant information.
I considered the problem of getting the initial data, processing and sorting beyond the scope of this test.
Using a third party API was the best solution in order to focus on the problem of commenting, vote, thumbs down for restaurant which was explicitly asked by the stake holders.

For future references: The list of restaurant retreive from Factual.com is sorted by "placerank": http://developer.factual.com/search-placerank-and-boost/#placerank
