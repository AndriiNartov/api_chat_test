## TEST TASK
### Simple public chat application(only RESTful API)
Object of this task is to create a simple REST API. API was created using Django Rest Framework.



### Technologies:
* Python 3.9
* Postgresql
* Django
* Django Rest Framework
* GIT
* Travis CI
* Heroku

### Set up and run project:
By default this application uses PostgreSQL. If you do not want to install postgresql on your machine,
you can run postgresql in docker container. For this purpose was created docker-compose.yml file.
To run postgres in docker container you should change your work directory to 'api_chat_test'
and run the command:
```
docker-compose up
```

To run the application you should activate your virtual environment(if you are using it) and run commands:

```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
After running the application you can go to http://127.0.0.1:8000/.
Now you can see a list of URL addresses with description which you can use to make requests to the server.

Project also was deployed on Heroku server https://api-chat-test-task.herokuapp.com/ and you are able to make requests to this service. After every new push to GIT repository https://github.com/AndriiNartov/api_chat_test
build is automatically passes the checking and testing by Travis CI and if build passes successfully,
new code will immediately deploy on Heroku.

### Tests
You are also able to run tests in the project manually. Make sure that your postgres db is available for connection
and your postgres user has role to create databases. To check if application passes tests run the command:
```
python manage.py test
```
### Important

You can find .env file in this repository. It was included here to make you run the project less complicated.
In case of real project you must 'hide' your sensitive data (SECRET_KEY,access db credentials, etc.)
and not show it in public repository.


[![Build Status](https://app.travis-ci.com/AndriiNartov/api_chat_test.svg?branch=main)](https://app.travis-ci.com/AndriiNartov/api_chat_test)