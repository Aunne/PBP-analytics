FROM selenium/standalone-chrome:latest
MAINTAINER Star Inc.<star_inc@aol.com>

WORKDIR /app
COPY . /app

RUN sudo apt-get update
RUN sudo apt-get upgrade -y
RUN sudo apt-get install -y python3.7 python3-pip
RUN python3.7 -m pip install --upgrade pip
RUN python3.7 -m pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 2020

CMD ["python3", "main.py"]