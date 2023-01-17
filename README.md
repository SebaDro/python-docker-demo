# Python Docker Demo
This project simply demonstrates how to create and run a Docker container that provides a Flask-based web service.
## Get Started
### Inspect the Dockerfile
The Dockerfile is a template that defines how to create a Docker image when calling `docker build`. The Dockerfile for this project is as simple as possible and contains the instructions listed below:
* `FROM python:3.8-slim-buster`: Python parent image, which contains all needed system libraries to run Python applications.
* `WORKDIR /app`: Creates and sets _/app_ the working directory inside the image.
* `ENV FLASK_APP=demo`: Sets an environment variable. The `FLASK_APP` variable is needed to tell Flask the app name.
* `COPY requirements.txt requirements.txt`: Copies the _requirements.txt_ into the image.
* `RUN pip3 install -r requirements.txt`: Calls `pip install` to install all required dependencies within the image.
* `COPY . .`: Copies all other source files into the image
* `CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]`: Default command, when starting the container. This command will run the Flask server at startup.
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
The Flask web server listens on port `5000` inside the container. The `-p` argument defines a port mapping, which exposes port `5000` on your host machine. To choose another port for your host machine just adopt the argument value, such as `-p 8080:5000`.
### Call the Web Service
Congratulations! You just set up your first Python web application with Docker. Now you can call the web service via:
[http://localhost:5000/greeting?name=Demo](http://localhost:5000/greeting?name=Demo)
### Use Docker Compose
As you already now how to build an image and run a container from it, it's time to automate container configurations via Docker Compose. For this purpose, you'll find a [docker-compose.yml](./docker-compose.yml) within the repository.

The docker-compose file simply defines a single service, which will be started from the _python-docker-demo_ image. It also defines a port mapping so that the service will be available under port 8000 on you host. You may also notice an `environment` section. This section contains the definition of the `CUSTOM_GREETING` environment variable to set a custom greeting phrase. You may want to set your own phrase here. Just change the current value.

To run the container with docker compose, first stop the running container, if not already done, with `ctrl+c`. Then call `docker compose up` from the root of the project directory. As a result, the service now is accesible via:
[http://localhost:8000/greeting?name=Demo](http://localhost:8000/greeting?name=Demo).
