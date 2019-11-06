# Guess the World Web-app help sheet
## Introduction
Welcome to the Guess the World web-app, the app which will help you learn more about the world in which you live in.
This help sheet will show you the many ways in which you can upload the application.
### Tools used
This application was run using an Ubuntu instance on GCP, it uses Python as its main scripting language, specifically the Flask web-framework which uses normal HTML and CSS along with JINJA2 syntax to impliment the pythonic logic that was created in the python files 

## GCP Firewall Rules
1. Click the 3 dots on the side of your VM and on the drop down go to Network details
2. Then on the side menu click **Firewall Rules**
3. Now you should click **Create new firewall rule**
4. Change the Targets to **All instances on the Network**
5. Input **0.0.0.0/0** in the source IP range
6. tick the tcp checkbox and enter **5000** in the box next to it

## Prerequisite
1. Have Python3 installed on your machine by using **sudo apt-get install python**
2. Make sure your apt-get is up to date by inputing **sudo apt-get update**
3. Install pip3 by using: **sudo apt-get install python3-pip**
4. Have Jenkins already installed (only for Jenkins pipeline upload)
5. Clone this repository to your machine

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

### Jenkins pipeline
1. In your Vm add a new user called pythonadm using,
    **sudo useradd -m -s /bin/bash pythonadm**
2. Check whether jenkins and pythonadm have access to the document by using,
    **sudo visudo**
3. If not input:
```
jenkins  ALL=(ALL:ALL) NOPASSWD:ALL
pythonadm  ALL=(ALL:ALL) NOPASSWD:ALL
```
4. In Jenkins create a new pipeline task.
5. In the pipeline definition switch it to *Pipeline script from SCM* and select the SCM as git.
6. In the repository URL enter this repository URL and then select save.
7. Now press build now and the app should start to set up.
#### Congratulations you have now got a working version of the Web-app
