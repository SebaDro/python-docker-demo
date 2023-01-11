# Python Docker Demo
This projects simply demonstrates how to create and run Docker containers that provide a Flask-based web service.
## Get Started
### Create a Dockerfile
The Dockerfile is a template that defines how to create a Docker image when calling `docker build`. The Dockerfile for this project is as simple as possible
and contains the instructions listed below:
* `FROM python:3.8-slim-buster`: Python parent image, which contains all needed system libs to run Python applications.
* `WORKDIR /app`: Creates and sets _/app_ the working directory inside the image.
* `ENV FLASK_APP=demo`: Sets an environmen variable. The `FLASK_APP` varibale is needed to tell Flask the app name.
* `COPY requirements.txt requirements.txt`: Copies the _requirements.txt_ into the image.
* `RUN pip3 install -r requirements.txt`: Calls `pip install` to install all required dependecies withing the image.
* `COPY . .`: Copies all other source files into the image
* `CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]`: Default command, when starting the container. This command will the Flask server at startup.
### Create a Docker Image
To create a Docker Image from the Dockerfile just call the `docker build` command, as follows:  
```
docker build -t n52/python-docker-demo:dev .
```
The `-t` argument provides a name for the image when building it locally on your host machine. To choose a different name, simply adjust the tag `n52/python-docker-demo:dev`.  

The `.`, at the end of the command, defines the directory, in which to execute the command. Docker searches for a _Dockerfile_ inside this directory and creates an image according to it.
### Run a Docker Container
To create a new container from the previously created image, use the `docker run` command:
```
docker run -it -p 5000:5000 n52/python-docker-demo
```
The Flask web server listens on port `5000` inside the container. The `-p` argument defines a port mapping, which exposes port `5000` on hour host machine. To choose another port for your host machine just adopt the argument value, such as `-p 8080:5000`.
### Call the Web Service
Congratulations! You just set up your first Python web application with Docker. Now you can call the web service via:
[http://localhost:5000/greeting?name=Demo](http://localhost:5000/greeting?name=Demo)
