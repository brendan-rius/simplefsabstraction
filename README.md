# simplefsabstraction

Provides a very simple filesystem abstraction.
Does not aim to be exhaustive from the beginning, please feel free to request/add the abstractions you need.

Supports:
 * local
 * S3

Inspired by `pyramid_storage`, but this one is not hardwired to pyramid.

# Installation

Requires:
 * python3

```
$ git clone https://github.com/brendanrius/simplefsabstraction/
$ pip install simplefsabstraction
```

# Changelog

 * 1.3.0: `save()` can now handle the case where the source file is a file, now just a filename