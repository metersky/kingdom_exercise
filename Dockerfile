FROM python:3.9
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt 
RUN chmod +x ./start.sh