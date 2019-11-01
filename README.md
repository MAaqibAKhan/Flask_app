# Guess the World Web-app help sheet
## Introduction
Welcome to the Guess the World web-app, the app which will help you learn more about the world in which you live in.
This help sheet will show you the many ways in which you can upload the application.
### Tools used
This application was run using an Ubuntu instance on GCP, it uses Python as its main scripting language, specifically the Flask web-framework which uses normal HTML and CSS along with JINJA2 syntax to impliment the pythonic logic that was created in the python files 

## Prerequisite
1. Have Python3 installed on your machine
2. Make sure your apt-get is up to date
3. Install pip3 by using: **sudo apt-get install python3-pip**
4. Clone this repository to your machine

## Running the app
### Local Machine
1. cd into the Flask app folder
2. do **pip3 install -r requirements.txt** 
3. to run the app use **python3 run.py**

### Docker
1. Upload docker onto your machine using 
     **curl https://get.docker.com | sudo bash**
2. So that docker does not need to use sudo use:
     **sudo usermod -aG docker $(whoami)**
3. Use **docker build -t flask-app .** to build the docker image
4. Use **docker run -d -p 5000:5000 flask-app**

### Making sure jenkins can run it
1. Add a new user called pythonadm using 
    **sudo useradd -m -s /bin/bash pythonadm**
2. Check whether jenkins and pythonadm have access to the document by using
    **sudo visudo**
3. If not input:
```
jenkins  ALL=(ALL:ALL) NOPASSWD:ALL
pythonadm  ALL=(ALL:ALL) NOPASSWD:ALL
```
#### Congratulations you have now got a working version of the Web-app
