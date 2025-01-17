FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

CMD python manage.py runserver 0.0.0.0:$PORT
