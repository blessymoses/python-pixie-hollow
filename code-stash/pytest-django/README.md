## Testing Trivia

- Unit Test
  - Tets units in isolation
  - Fixed input produces a known fixed output
  - Any external dependency should be mocked
  - Can simulate errors

- Integration test
  - Test multiple components
  - Tests the contract between them
  - Test with narrow inputs

- E2E
  - Test the end-to-end flow of the system
  - Test if the entire system works correctly
# Django Rest Framework
- Install Django Rest Framework
```sh
$ pip3 install djangorestframework
$ python3 -m django --version
3.2.3
```
## Create a project
+ A project is a collection of configuration and apps for a particular website. 
+ A project can contain multiple apps.
1. Create a django project
```sh
$ django-admin startproject mytestproject
```
2. To run the development server
Navigate to "mytestproject"
```sh
$ python manage.py runserver
```
3. To run the migrations
```sh
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```
4. Create an admin user
```sh
$ python manage.py createsuperuser
Username (leave blank to use 'blessy'): 
Email address: myemail@example.com
Password: 
Password (again): 
Superuser created successfully.
```
## Create the app
+ An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app.
+ A project can contain multiple apps. 
+ An app can be in multiple projects.
1. To create your app, make sure you’re in the same directory as `manage.py` and type this command:
```sh
python manage.py startapp companies
```