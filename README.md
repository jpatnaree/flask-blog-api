# Flask Blog API

This is a simplified json API for a blog site. Currently it only has two tables, one for users and one for blogs. Users and blogs have a one to many relationship. In other words, a user can have many blog, but a blog has only one user (that is, belongs to only one user).


## Setup

1. (Fork)/Clone the repo
2. cd into directory
3. run `pipenv install`
4. run `pipenv shell`
5. run `python app.py` to make sure the server is working
6. stop the server with ctrl+c, then run the following three commands:
    - `flask db init`
    - `flask db migrate`
    - `flask db upgrade`
7. run `python seed.py`

## Exploring the Code
After completing the setup, and **before** starting the tasks, you should familiarize yourself with the code. Here are some ways of doing that:
- Run the `curl` commands in the `requests` file.
    - Don't forget to put print/debugger statements in the code if you are not sure what is happening
    - Find out the types of all variables/parameters
- Run the seed file with added print/debug statements
- In your terminal, run `flask shell`. This will allow you to create database objects (e.g. `User` and `Blog`) and experiement with them 
## Tasks
- Create a database schema diagram using [this tool](https://dbdiagram.io/)
- Fill in routes for blogs. The routes for users are completed, so use them as a guide
- Create a new model called `Comment`
    - it will have the following column names:
        - id (integer, primary key)
        - user_id (integer, foreign key to user_table)
        - content(string)
    - it will have a many to one relationship with blog (i.e. a blog can have many comments, but a comment can only be on one blog)
- Update your database diagram to include `Comment`
