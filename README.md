# Resto
A restaurant app for fueled (test)


## Dev Installation

Create a virtual env with virtualenv wrapper

    $ mkvirtualenv resto

Activate the environment:

    $ workon resto

Clone/Download this repo:

    $ git clone git@github.com:rafen/resto.git

Enter to the just clonned repo:

    $ cd resto

Install requirements by entering to the repo folder and run

    $ pip install -r requirements.txt

Initialize your local database:

    $ ./manage.py migrate

Create a superuser:

    $ ./manage.py createsuperuser

Enter username, email and password


Import Restaurants (This command will only import 500 restaurants to the system, after that it will raise an error, see section "Import Restaurants into the system" for more info):

    $ ./manage.py import_restaurants


Run a local test server:

    $ ./manage.py runserver

Visit the backend test landing page by opening your browser at

    http://localhost:8000


## Usage:

The system has Django Back-end, a landing page served by Django and a static app that use the endpoints provided by the backend.
To start using the system you can visit the landing page served by Django at:

    http://localhost:8000

### Landing: http://localhost:8000
![Landing Page](https://dl.dropboxusercontent.com/u/14133267/resto/Resto-Landing.png)

There you will find links to navigate to the other pages and apps

### Django Admin: http://localhost:8000/admin/
Standard Django Admin to mange models and create users

### Browse API Doc: http://localhost:8000/api-docs/
![Django Swagger for Rest framework](https://dl.dropboxusercontent.com/u/14133267/resto/Resto-API-Doc.png)

### Test Client site: http://localhost:8000/static/ui/index.html#/
Search Page of restaurants
![Search page of restaurants](https://dl.dropboxusercontent.com/u/14133267/resto/Resto-Search.png)

Restaurants detail page
![Restaurant detail page](https://dl.dropboxusercontent.com/u/14133267/resto/Resto-Details.png)

### Loging:
In order to use the test site you need to be logged in (if not you won't be able to modify any data). To do that you can use the links provided on the site or use this link: http://localhost:8000/api-auth/login/?next=/

In the test pages users can:

 * Login / Logout
 * See a list of restaurants (paginated by 10)
 * Search by type of cuisine and name of the restaurant
 * Order restaurant list by ID, name, Thumbs down, and rating. To do this a user needs to click on the table head, if a user clicks again the ordering is removed. Thumbs down column is order incrementally, so if a user click on it he won't see Restaurants with Thumbs down at the top.
 * See the details of a restaurant. If a user click on the name of a restaurant, the page will scroll down and the details of the restaurant will be shown.
 * In the details of a restaurant a user can:
  * Thumbs Down/Up the restaurant (the Up only works as an undo of the thumbs down)
  * Mark the restaurant as vistied
  * Leave a comment (the comment will be displayed at the top of the comment list)

## Running tests

To run the backend test just type:

    $ ./manage.py test


## Technology
 * Django and Python are used in the backend.
 * Django Rest Framework is used to build the API.
 * Django Swagger was installed to provide a better documentation for the API.
 * Django-vote is used to manage the thumbs down functionality.
 * Factory-boy is used to simplify the testing of the models, and can be used in the future for performance tests.
 * Factual app is used as an adapter to communicate with Factual.com API and retreive the restaurants (see section "Import Restaurants into the system" for more information about why using Factual).
 * Yeoman was used to start the frontend app.
 * Angular and coffee script are used to code the app.
 * Grunt was used during the development of the frontend app, and also for the distribution of it.


## About the API
The API is built on django rest framework.
The endpoints were designed to minimize the amount of requests made to the backend.
The main endpoint is /restaurants/restaurant/ that will return a page (of 10 elements) with almost all the information needed to display a list of restaurants, with visitor comments, etc
The API also has other endpoint to create comments, votes, visits, etc. Almost all of them are based on the Django Model which reduce the amount of code and logic on the system.


## Import Restaurants into the system
Factual.com is used to get the restaurant information.
I considered the problem of getting the initial data, processing and sorting beyond the scope of this test.
Using a third party API was the best solution in order to focus on the problem of commenting, vote, thumbs down for restaurant which was explicitly asked by the stake holders.

For future references: The list of restaurant retreive from Factual.com is sorted by "placerank": http://developer.factual.com/search-placerank-and-boost/#placerank


## Frontend App for testing:
In resto-ui folder you will find the frontend app to test the application.
The distribution folder of the front-end app is already included and linked in the static folder of the repo, but if you need to work on it, you can do this:
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
