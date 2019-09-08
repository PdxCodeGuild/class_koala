# Capstone Proposal

The below is the proposal for my capstone project. The deadline for the initial MVP is Friday, September 27th, with presentations likely taking place the week of Monday, October 14th.

## Name

**Food Cart City** - Following in the footsteps of Rose City, Rip City, Bridge City, etc., the #1 destination for food carts in the country deserves yet another nickname, alongside a dedicated app

## Project Overview

**What are the major features of your web application?**
* Displays Google map of Portland with icons for each food cart, as well as distinct colorings for each neighborhood
* Allows for filtering of food carts based on various criteria: _Neighborhood, Cuisine, Distance, Price & Operating Hours_
* When selected, each food cart will display their name, photo, description, contact info and menu
* User management system, with ability to login to select favorites, as well as a customer history to store notes on carts previously visited and meals previously tasted

**What problem is it attempting to solve?**
* The app is intended to simplify the process of locating a food cart in Portland
* It will also declutter the search and allow for easier access to the most pertinent information

**What libraries or frameworks will you use?**
* The backend will be handled with Django and SQLite
* Much of the data will be acquired with Yelp API
* Google API will be needed to operate the map and geolocation
* The front-end display will either be written with vanilla CSS or Bootstrap
* Interaction will be handled by either vanilla JavaScript or Vue.js

## Features

### User Story #1:
* As a fan of food carts, I want a way to quickly see all of the food carts in Portland because I would be interested in eating at one and want to see what options are available.

### Tasks:
* Gather the data of the food carts in Portland / store in model table
* Display back to user in gallery format

## Functionality Questions:

**What will the user see on each page?**
* There will essentially be one main page. This will display the map, the filters and the full listing of the food carts
* There will also be a top header bar, which will feature the logo, app name, a search feature, login option and create an account option

**What can they input and click and see?**
* The user will be able to zoom in and out of the map, click the icons to display info on the food carts, click the various filters and select a drop-down option and click on the food cart squares to also display info on the relevant food cart. They can also search for food carts by name, sign in and register for an account.

**How will their actions correspond to events on the back-end?**
* Users will not be able to edit the food cart database itself, as this information would only change if the food cart themselves either moved, closed, changed their menu, prices, etc.
* The user's clicks on different filters would activate various views.
* The users would also be able to create an account, edit their profile, select favorite food carts, select visited carts, add notes, etc. This woud be tied solely to their profiles.

## Data Model

* **User:** Username, First Name, Last Name, Email, Password
* **Profile:** Display Name, Photo, Neighborhood, Favorite Cart(s), Visited Cart(s)
* **Carts:** Name, Photo, Address, Phone Number, Website, Neighborhood, Cuisine, Price Range, Operating Hours, Menu

## Schedule

### Cycle One: Bare Bones MVP

* **Backend** Import all food cart data into database, potentially with Yelp API _(Build or update incomplete details, where necessary)_
* **Frontend** Create simple navbar - just name of the app, plus logo, if ready
* **Frontend** Create filter bar with dropdowns _(Hide the filters not yet programmed - all to start)_
* **Frontend** Create the section for the food cart gallery
* **Backend** Display all of the carts in the dedicated gallery, likely using a for loop
* **Frontend** Create a window pop-up / detail view and enable it to be displayed when food cart square is clicked

## Ranking The Product Backlog

* **Essential Features:**
  * Display all of the food carts in a gallery-style view
  * Click on a food cart square and all of the pertinent information regarding each food cart is displayed
  * Filter by various metrics _(Neighborhood, Cuisine, Distance, Price, Hours)_
* **Really-Great-To-Haves:**
  * User location functionality - locate user, ascertain distance to respective food carts
  * Google Map with icons for each food cart
  * Distinct neighborhood boundaries on the Google Map
  * User Managemen System with ability to mark favorite and visited food carts
* **Nice-To-Haves:**
  * Expanded user management system with ability to write internal reviews on food carts / specific dishes
