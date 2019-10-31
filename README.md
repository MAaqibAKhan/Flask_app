# Guess the World Web-app help sheet
## Prerequisite
1. Have Python3 installed onto the VM
1. Clone this repository to your machine

## Installing Docker
1. Upload docker onto your machine using 
     **curl https://get.docker.com | sudo bash**
2. So that docker does not need to use sudo use:
     **sudo usermod -aG docker $(whoami)**

## Running it in docker
1. Use **docker build -t flask-app .** to build the docker image
2. Use **docker run -d -p 5000:5000 flask-app**

## Making sure jenkins can run it
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
