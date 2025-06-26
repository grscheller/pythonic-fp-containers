# Pythonic FP - Containers

Container based data structure, part of the
PyPI
[pythonic-fp](https://github.com/grscheller/pythonic-fp/blob/main/README.rst)
Namespace Projects.

Detailed API
[documentation](https://grscheller.github.io/pythonic-fp/maintained/containers)
on *GH-Pages*.

## Features:

### Single item box - dtools.containers.box

Container holding at most one object of a given type. This stateful
(mutable) container can contain only 0 or 1 items. Invariant in its
contents. Both ``map`` and ``bind`` return new objects. Iterable.

### Functional tuple - dtools.containers.functional_tuple 

Subclassed tuple with a more functional interface. Gives tuple FP
methods. Designed to be further inherited from. Hashable if all
contained items are hashable.

### Immutable list - dtools.containers.immutable_list

A hashable, immutable, list-like data structure. Hashability will be
enforced when instantiated. Mutable list methods will return new
objects.

### Maybe monad - dtools.containers.maybe

An implementation of the maybe (or optional) monad. Data structure
represents a possibly missing value. Useful in implementing exception
free code paths.

### Either monad - dtools.containers.xor

An implementation of a left biased either monad. Data structure
representing either a "left" or "right" value, but not both. These two
values can be the same or different types. The "left" value is usually
taken to be the "happy path" of code flow. The "right" value is often
used for an error condition or a text string describing what went wrong.

## Installation:

```
    $ pip install pythonic-fp.containers
```

## Contribute:

- Project on PyPI: https://pypi.org/project/pythonic-fp.containers
- Source Code: https://github.com/grscheller/pythonic-fp-containers
- Issue Tracker: https://github.com/grscheller/pythonic-fp-containers/issues
- Pull Requests: https://github.com/grscheller/pythonic-fp-containers/pulls
- CHANGELOG: https://github.com/grscheller/pythonic-fp-containers/blob/main/CHANGELOG.rst

| Contributors | Name | Role |
|:------------ |:---- |:---- |
| [grscheller](https://github.com/grscheller) | Geoffrey R. Scheller | author, maintainer |


### License Information

This project is licensed under the Apache License Version 2.0, January 2004.

See the
[LICENCE file](https://github.com/grscheller/pythonic-fp-containers/blob/main/LICENSE)
for details.
