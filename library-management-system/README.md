
# Project

Library Management System (Python - DjangoFramework)

# Description

I build a library management system using Django where an admin can
perform CRUD ( create, read, update and delete) operations like

- Add a Book
- Update an entry of a book
- Delete a book
- Get all books

using Python (Django Framework) 

## Requirements
- asgiref==3.2.7
- Django==3.0.5
- django-widget-tweaks==1.4.8
- pytz==2020.1
- sqlparse==0.3.1

**documentation for backend code**

For Backend We used these Technologies
- Python - install python on your system.

It is best practice to provide a dedicated environment for each Django project you create.
- To create a virtual environment for your project
```bash
   py -m venv project-name
```
- To activate the environment
```bash
    project-name\Scripts\activate.bat
```
- Django (Framework) - to install use this command, ensure your virtual environment is active
```bash
  py -m pip install Django
```
- Mysql (database) - to install use this command
```bash
  pip install mysqlclient
```
- MySQLClient is basically an adapter used for interacting with Django ORM (Object Relational Management). Basically it is going to install Django code which is needed to connect with the database. 

**Instructions to Execute the Project**
- Install the Requirements:
```bash
  pip install -r requirements.txt
```
-- Then run 
```bash
  python manage.py makemigrations
```
```bash
  python manage.py migrate
```
**Finally it's time to create superuser/admin who will be managing students and books!**
Run 
```bash
python manage.py createsuperuser
``` 
and enter the required data.
After that run 
```bash
  python manage.py runserver
```
 and head over to the browser to http://127.0.0.1:8000 and login.

## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)




There are two types of user one is superuser/admin and another is regular user/students.
Superuser/Admin can add students, add books, issue books to student, delete the returned book, edit and delete books and students profile.

While, student can login and see books list and the books issued by them.
To register students have to fill up a information form and after that admin can view the informations sent by student in admin site and add a new student based on the details filled by the students in the information form if he/she is verified student of the given organizations.
Then admin will send the credentials created by them via email to the student and using those credentials student can login to the library.

Before adding new books please go to the http://127.0.0.1:8000/admin admin site and add the required genre and language manually as we cannot add genre and language through the site. And visit the admin site to see information form regularly as if someone had registered for the library.
