# python_project
Overview
This application allows users to add, edit, view and delete houses/apartments that available for rent in des moines area

Project Links
GitHub: (https://github.com/kpendurthi/python_project)


MVP - Bronze
View list of houses/apt available for rent
Add/Edit a houses/apt 
update house name
update house rent amt
update house image 
delete house/apt


View list of citys
Add/Edit cities list
update city name
delete city


add authentication for users to update/edit/create/delte houses/apt 

User Stories
as a user, I can view a list of hosues/apt or cities
as a user, I can add/edit a hosues/aptfrom the home page
as a user, I can add/edit hosues/apt name ,image, amt and city name
as a user, I can delete existing houses/apt available for rent

Models
Table City

Field	Property
name	character field


Table houses

Field	Property
city	foreign key
name 	CharField
amt	CharField
image url	CharField
addres CharField
description	text area

Issues and Resolutions
Use this section to list of all major issues encountered and their resolution.

#4 - Issue with deploying my application via Heroku