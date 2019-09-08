# Capstone Proposal

The below is the proposal for my capstone project. The deadline for the initial MVP is Friday, September 27th, with presentations likely taking place the week of Monday, October 14th.

## Name:

**Food Cart City** - Following in the footsteps of Rose City, Rip City, Bridge City, etc., the #1 destination for food carts in the country deserves yet another nickname, alongside a dedicated app

## Project Overview

**What are the major features of your web application?**
* Displays Google map of Portland with icons for each food cart
* Allows for filtering of food carts based on various criteria
* Neighborhood, Cuisine, Distance, Price & Operating Hours
* When selected, each food cart will display a photo, description, contact info and menu

**What problem is it attempting to solve?**
* The app is intended to make locating a food cart quicker, easier and simpler

**What libraries or frameworks will you use?**
* The backend will be handled with Django and SQLite
* Much of the data will be acquired with Yelp API
* Google API will be needed to operate the map and geolocation

## Features

### User Story #1:
* As a tourist, I want a listing and location of the food carts in Portland because I want to eat at one near to me.

#### Tasks:
* Gather the data of the food carts in Portland / store in model table
* Obtain the location of the user
* Filter carts based on nearest location to user
* Display back to user

##### Functionality Questions:

**What will the user see on each page?**
* There will essentially be one main page. This will display the map, the filters and the full listing of the food carts

**What can they input and click and see?**
* The user will be able to zoom in and out of the map, click the icons to display info on food cart, click the various filters and select a drop-down, click on food cart squares to display the same info as previous. They can also search for food carts by name, sign in and register.

**How will their actions correspond to events on the back-end?**
* Apart from creating an account and editing a profile, users will not be able to edit the food cart database. I am exploring a favorite feature, but this would come later and would still be attached to the user’s profile.
* The user’s clicks on different filters would activate various views

## Data Model

**User:** Username, First Name, Last Name, Email, Password
**Profile:** Photo, Location or Neighborhood, Favorite Cart(s)
**Carts:** Photo, Name, Address, Neighborhood, Cuisine, Price Range, Operating Hours, Menu

## Schedule

### Cycle One: MVP

* Import all food cart data
* Create simple navbar - Just name of app
* Create filter bar with dropdowns
* Create display section
* Write programs to filter by each selection

**Essential Features:**
**Really-Great-To-Haves:**
**Nice-To-Haves:**
