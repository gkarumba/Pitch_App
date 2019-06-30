# Pitch App

This project was generated with python version 3.6.

### By Gkarumba

##  Description
This is a python web appliction that allows a user to create an account, log into it and publish as well as read pitches posted by other users. the application also allows users to comment on pitches once logged in.


## User Stories
These include the features that the application allows.
The user is able to:
* sign up for an account and log in .
* create new category and save them
* See other peoples categories and post comments in them


## Prerequisites
To develop the application , youll need to preinstall a few application. including
* python 3.6
* flask
* pip
* postgress

## Technologies Used
* python 3.6 
* postgress

## Setup Information
* Clone the application repository to your local machine .
* Create a new virtual environment and access the folder through your virtual amchine.
* access the code through your preffered code editor
* create your database and link it in the config.py
* run this on your terminal python3.6 manage.py server
* Run chmod +x start.sh follwoed by ./start.sh while in the project folder to start the project.
* Once run, the project can be accessed on your localhost using the address: localhost:5000.

## BDD
|Behavior |Input |Output |
|:------------| :---------|:--------|
| user signs up | fills sign up form on entry | home page displayed and user can access and add categories|
|user logs in |user enters credentials and password|home page displayed and user can access and add categories|
|create pitch category |click on create category |redirected to page where user can create new pitches with regards to the category|


## LICENSE
MIT License

Copyright (c) 2019 gkarumba