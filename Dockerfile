FROM python:3.8-slim-buster

WORKDIR /app

ENV FLASK_APP=demo

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# docker build -t n52/python-docker-demo .
# docker run -it -env CUSTOM_DEMO_GREETING="Custom greeting text!" -p 5000:5000 n52/python-docker-demo