# simplefsabstraction

Provides a very simple filesystem abstraction.
Does not aim to be exhaustive from the beginning, please feel free to request/add the abstractions you need.

Supports:
 * local
 * S3

# Installation

Requires:
 * python3

```
$ git clone https://github.com/brendanrius/simplefsabstraction/
$ pip install simplefsabstraction
```

# Contribute

The tests are made to be run in Docker (to not mess with the local filesystem):

```
$ CONTAINER_ID=$(docker build .) (to be done only once)
$ docker run $CONTAINER_ID
```

You can run the tests without Docker (at your own risk):

```
python setup.py test
```