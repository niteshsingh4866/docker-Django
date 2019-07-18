FROM python:3-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
# Installing client libraries and any other package you need
RUN apk update && apk add libpq
# Installing build dependencies
RUN apk add --virtual .build-deps gcc python-dev musl-dev postgresql-dev

RUN pip3 install -r requirements.txt
# Delete build dependencies
RUN apk del .build-deps
COPY . .
EXPOSE 8000
CMD ["python","manage.py", "runserver","0.0.0.0:8000"]
# CMD ["python manage.py makemigrations","&&","python manage.py migrate" ,"&&","python manage.py runserver 0.0.0.0:8000"]
