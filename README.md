# hotel_api
Useful Django commands

* sudo easy_install django or pip install django 	      > install Django
* django-admin —-version or pip show django 		        => check Django version
* which django-admin 					                          => path to Django
* django-admin startproject <project_name> 		          => create new Django project
* virtualenv -p <path_to_python> --distribute venv 	    => create virtual environment
* . venv/bin/activate/					                        => activate virtual environment
* python manage.py startapp <section_name>		          => add new app
* python manage.py makemigrations <app_name>		        => create migrations
* python manage.py sqlmigrate <app_name> <version>	    => create SQL scripts
* python manage.py migrate				                      => apply migrations
* python manage.py shell				                        => enter Django database shell
* python manage.py createsuperuser			                => create superuser to login on Django admin panel
* python manage.py runserver				                    => run Django development server
