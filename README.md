# postgres_orm_template
A bare bones implementation of SQL Alchemy's ORM. This is designed to be a template to help others and myself get new projects up and running quickly. The tables and queries are taken from SQLAlchemy's site here: http://docs.sqlalchemy.org/en/latest/orm/tutorial.html

All you need to do to get a database up and running is to install postgreSQL and SQLAlchemy (use pip). Once the postgreSQL server is installed, make sure it is running by logging into it using the commandline psql. 
Create a user and a database. 

Replace the username, password, and database name with yours and run it main.py. When everything is configured properly you should see two tables newly created in your database called users and addresses with some data in them. They have a simple relationship between them and some examples queries to get you started.
