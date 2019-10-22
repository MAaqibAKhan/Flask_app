# Guess the World Web-app help sheet

1. Clone this repository to your machine
2. To get to the Virtual environment (venv) type: **cd Flask_app/application/**
3. Activate the venv by typing: **. venv/bin/activate**
4. Once in the venv go back to the Flask_app folder
5. If you haven't done so do **sudo apt-get update**
6. Now you will need to install all of the applications below:
     ```
     sudo apt-get install python-pip
     pip install flask
     pip install flask-login
     pip install flask-wtf
     pip install flask-sqlalchemy
     pip install flask-bcrypt
     pip install pyopenssl
     ```
7. the next commands you will need to use to make sure that the code will work on Browser
     ```
     openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
     export FLASK_APP=run.py 
     export FLASK_ENV=production 
     export FLASK_RUN_HOST=0.0.0.0 
     export FLASK_RUN_PORT=5000 
     export FLASK_RUN_CERT=cert.pem 
     export FLASK_RUN_KEY=key.pem
     flask run
     ```
     
#### Congratulations you have now got a working version of the Web-app
