FROM python:2.7.15-slim-jessie

RUN pip install pipenv && \
mkdir /sdpw

WORKDIR /sdpw
COPY sdpw/Pipfile /sdpw/Pipfile
COPY sdpw/Pipfile.lock /sdpw/Pipfile.lock
COPY ./sdpw/Book/ /sdpw/Book

RUN pipenv install --deploy --python=$(which python)

ENTRYPOINT ["pipenv", "run", "python", "/sdpw/Book/book.py"]
EXPOSE 80