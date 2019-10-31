# Guess the World Web-app help sheet

1. Clone this repository to your machine
2. Upload docker onto your machine using 
     **curl https://get.docker.com | sudo bash**
3. So that docker does not need to use sudo use:
     **sudo usermod -aG docker $(whoami)**
4. cd into the Flask_app folder
5. Use **docker build -t flask-app .** to build the docker image
6. Use **docker run -d -p 5000:5000 flask-app**

#### Congratulations you have now got a working version of the Web-app
