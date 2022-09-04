FROM python:3.10-slim

WORKDIR app/
COPY poetry.lock .
RUN pip install poetry
RUN poetry update

COPY . .
CMD python manage.py runserver 0.0.0.0:8000 --settings=todolist.settings
