# hotel_api
Useful Django commands

* Install Django by using `sudo easy_install django` or `pip install django`
* Check Django version with `django-admin —-version` or `pip show django` 		        
* Check Django path with `which django-admin`					                         
* Create new Django project `django-admin startproject <project_name>`
* Create virtual environment by using `virtualenv -p <path_to_python> --distribute venv` 	    
* Activate virtual environment `. venv/bin/activate/`				                       
* Run `python manage.py startapp <section_name>` to add new app
* Run `python manage.py makemigrations <app_name>` to create migrations
* Run `python manage.py sqlmigrate <app_name> <version>` to create SQL scripts
* Run `python manage.py migrate` to apply migrations
* Run `python manage.py shell` to enter Django database shell
* Run `python manage.py createsuperuser` to create superuser to login on Django admin panel
* Run Django development server with `python manage.py runserver`
