FROM python:3.9-alpine
LABEL Abdullah Mujahid

ENV PYTHONUNBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE=1.

RUN apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev

COPY ./requirements.txt /tmp/requirements.txt

WORKDIR /app
EXPOSE 7000


RUN pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

COPY ./app /app

ENV PATH="/py/bin:$PATH"

USER django-user
