FROM python:3

RUN echo "Hello world" > /tmp/existingfile

RUN mkdir /code
WORKDIR /code

COPY . .

# We don't want to re-install the dependencies everytime
VOLUME /code

CMD ["python", "setup.py", "test"]