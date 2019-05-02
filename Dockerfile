
FROM python:3.7.3-alpine3.9
RUN apk add --update libpq nginx
RUN apk add --virtual .build-deps gcc postgresql-dev python3-dev musl-dev libffi-dev openssl-dev make
RUN pip install pipenv
COPY Pipfile Pipfile.lock /
RUN pipenv install --system --deploy
RUN apk del .build-deps
RUN rm -rf /var/cache/apk/*
RUN mkdir /run/nginx
COPY site.conf /etc/nginx/conf.d/default.conf
COPY static /www/data/static
EXPOSE 8000 80
ADD . /
CMD sh -c "nginx && gunicorn -b 0.0.0.0:8000  -w 4 app:app"
