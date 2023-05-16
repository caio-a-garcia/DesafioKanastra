FROM ubuntu:20.04
ENV REFRESHED_AT 2023-05-15

RUN apt-get update -y; apt-get install -y python3 pip

COPY requirements.txt /opt/app/

WORKDIR /opt/app

RUN pip install -r requirements.txt

COPY ./src/app/ /opt/app

WORKDIR /opt

EXPOSE 8000

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]