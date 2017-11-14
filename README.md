# hotel_api
Hotel API project

- sudo easy_install django or pip install django 	    => instaliranje Django
- django-admin —-version or pip show django 		    => provjeriti verziju Djanga
- which django-admin 					                => putanja do Djanga
- django-admin startproject <project_name> 		        => kreiranje novog Django projekta
- virtualenv -p <path_to_python> --distribute venv 	    => kreiranje virtualnog okruzenja
- . venv/bin/activate/					                => aktivacija virtuelnog okruzenja
- python manage.py startapp <section_name>		        => dodavanje app-a odnosno novog modula u projekat (Django aplikacije su modularne)			
- python manage.py makemigrations <app_name>		    => kreiranje migracija
- python manage.py sqlmigrate <app_name> <version>	    => kreiranje SQL skripte za sinkovanje na bazi (ukoliko zelis da je direktno pastis na bazi)
- python manage.py migrate				                => apliciranje migracija
- python manage.py shell				                => komanda da odjes u database shell od Djanga i da pristupas objektima kao kada radis u kodu
- python manage.py createsuperuser			            => kreiranje superuser-a tj admin-a sa kojim se logujemo na admin panel
- python manage.py runserver				            => startovanje aplikacije preko Django dev servera