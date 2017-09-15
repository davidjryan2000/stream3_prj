# Mailo Power
This is an Ecommerce site with Stripe Payments, User Authentication and Blog. This project is a submission for Stream 3 of Code Institute's Bootcamp.
The aim of this project was to create an online print store for artist Mailo Power.  The client wanted a strong visual element to demonstate her work. All images in the 
home page and in the gallery are her original works.  The client is a strong advocate of social media.  A blog was included to keep fans updated and to keep site content fresh for search ranking purposes.
A twitter feed was included beside the blog, and instagram posts feature. The Artday theme was chosen as it provided a close fit for what the client required.  Regular consultation with the client 
allowed the design to evolve from the template into the final project. The template effectively acted as a wireframe fro design purposes.

## Live Demo

**Follow this link to view deployed version of the web app https://stream3.herokuapp.com**

## Built with 
1. Django framework
2. Python
2. HTML
3. CSS
4. Bootstrap
5. mLab database
6. ArtDay Theme from Themeforest https://themeforest.net/item/artday-creative-shop-template/14021721


#Django
Django is a high level Python framework that allows apps to be created quickly and efficiently. It is organised around a variation of the Model View Controller architecture,
called Model Template Views - the model represents the data model in a relational database, the template is the visual representation of the data to the end user and views 
define the logic that links the templates to the models. 



## URL's

urls.py at the project level, stream3_prj,gives the url patterns routes to views, either directly:

 `from search.views import do_search`

 `urlpatterns = [url(r'^search/', do_search, name='search')]`

Or for the Apps that have their own urls, via the 'include' function:

 `from accounts import urls as accounts_urls`

 `urlpatterns = [url(r'^accounts/', include(accounts_urls))]`

## Views

Views called via URLs are Python functions that perform the different actions required to make the Website function e.g. render a template, log someone in, log them out etc.

## Templates

The base.html page in the top-level templates folder is the base template used for all pages and includes all the links CSS/Bootstrap/Javascript etc. and the fully responsive navbar and footer that appears on all pages of the Website. 
It also contains:
```
{% block header %}
{% endblock header %}

{% block content %}
{% endblock content %}

{% block sidebar %}
{% endblock%}
```
Which allows other templates to be inserted in to that section (between the navbar & footer). Linking the base.html to templates within Apps, example below:
```
{% extends 'base.html' %}

{% block content %}

Code for the app goes in here & will appear between the navbar & footer from base.html

{% endblock content %}
```

## Apps

#### Home

The Home App renders the index.html template, which in turn calls the base.html template to present a full webpage with navbar, content and footer.

#### Accounts

The Accounts App is used for full user authentication. When users first visit the website they have two options under 'My Account' - Register if they have no account or Log In if they do. Once Registered/Logged in they can view their own profile that will display their username and email address they used to register with. The two options under 'My Account will then change to Profile or Log Out. It is possible for users to Subscribe to a monthly magazine - once clicked the subscribe function is called within the views.py in the Accounts App which connects with Stripe payments and if the card details are entered correctly into the form it will take a monthly payment from the user.

#### Products

The Product App display the Products that have been added via Django's admin panel.  In order to facilitiate new designs and media for example a print could be made on paper, diasec or perhaps in future on greeting cards or diarys,
design and media classes were created in the Products models.py. This allows the administrator to upload new design images and names together with media type and price.
These additions will then be sent directly to the gallery. 

#### Gallery
The Gallery app displays all the print images along with name and collection name. The inages can be selected which will bring the user to a product options page with product image and description.  The user can select then items to be added to the cart. Once items are added to cart the user is brought to the cart.html.


#### Cart

The Cart App brings together user validation, product selection and adjustment and payments. The Payments App then renders a form for a one-off Stripe payment. The billing details form on the cart page has been added for aesthetic purposes,
it is not yet active.  Stripe payments are configured and can be tested using test credit card number 4242424242424242. Once payment is submitted the user will be directed back to the  gallery (print store) page.

#### Blog
The blog app allows site users to follow the artists news and to participate discussion with like minded people. In models.py a Post class was created to enable the posts to be saved in the database.
Functions in views.py allow a list of posts to be maintained and new posts to be created and edited. Disqus is used to add to the user experience when interacting with the blog.



## Hosting

The App is hosted on Heroku with automatic deploys from GitHub

## Databases / Static Files

When running locally, SQLite database was used & static and media files were stored locally.
When deploying, Heroku Postgres was used as the server database & an Amazon S3 bucket was set up to host all the static files. settings.py file was amended for the database & static files to point to the online resources.


#### Artday Template
A lot of work was undertaken to insert the relevant code into the template to get eveything functioning correctly.  Not all elements of the template were used at this stage in the project. The intention is to continue and complete an order app to complete the delivery process.

##Testing
Testing was carried out locally and since deployment. Version control was carried out on Git and copies of the project were kept locally.


