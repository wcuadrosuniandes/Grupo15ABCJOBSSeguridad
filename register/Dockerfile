FROM python:3.9

ENV PYTHONUNBUFFERED=1

RUN mkdir /service
COPY register/ /service/register/
WORKDIR /service/register
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

EXPOSE 5003
ENV FLASK_APP=app.py
ENTRYPOINT [ "flask", "run", "-p 5003", "--host=0.0.0.0"]