# employee-webapp-django
This is a Django project where we can create the records for Employees.

1. Create Employee

![employee create](https://github.com/thedevsafaf/employee-webapp-django/assets/85129653/deb97d6a-a823-4ced-a9f8-8ac7f9d0601e)

2. Read Employee
   
![employee index](https://github.com/thedevsafaf/employee-webapp-django/assets/85129653/c6e2df21-9808-443c-af3f-a577f5697049)

3. Update Employee
   
![employee update](https://github.com/thedevsafaf/employee-webapp-django/assets/85129653/1d1bb45e-2e46-4d47-846f-1568d44a53ec)

4. Delete Employee
   
![employee delete](https://github.com/thedevsafaf/employee-webapp-django/assets/85129653/f43c8bbd-31c3-4e72-a287-4bc715e3b282)

First clone the repository from Github and switch to the new directory:

$ git clone git@github.com/USERNAME/<project_name>.git

$ cd <project_name>

Setup the project structure:
```
-sample (project folder)
        -src
              -sample (project name)
                      -sample (main app name)
                              -settings.py
                              -urls.py
                              -wsgi.py
                       -app1
                       -app2
                       -appn
                       -requirements.txt
                       -manage.py      
        -venv  
```
Activate the virtualenv for your project.

PROJECT CONFIGURATION if first time
========================================
install virtualenv first
```
pip install --user virtualenv 
```
create virtual environment named venv
```
python -m virtualenv venv
```
activate the venv using activate script
```
venv\Scripts\activate
```
install django in the same venv
```
pip install django
```
to see the installed packages
```
pip freeze
```
install the driver for interacting with PostgreSQL from the Python scripting language
```
pip install psycopg2
```
install postgres for the first time or use sqlite by default
```
depends on the OS

 setup postgres sql
 setup server, username, password, port no. etc
 create database
```
Install project dependencies:
```
$ pip install -r requirements/local.txt
```
Then simply apply the migrations:
```
$ python manage.py migrate
```
You can now run the development server:
```
$ python manage.py runserver
```


