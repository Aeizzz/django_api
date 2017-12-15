FROM python:3.6
ADD . /app
WORKDIR /app

RUN apt update && pip install -r /app/requirements.txt

EXPOSE 8000

CMD sh /app/deploy/run.sh
