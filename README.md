# Pythonic FP - Containers

Container based data structure, part of the
PyPI
[pythonic-fp](https://github.com/grscheller/pythonic-fp/blob/main/README.rst)
Namespace Projects.

Detailed API
[documentation](https://grscheller.github.io/pythonic-fp/maintained/containers)
on *GH-Pages*.

## Features:

### Single item box - `pythonic_fp.containers.box`

Container holding at most one object of a given type. This stateful
(mutable) container can contain only 0 or 1 items. Invariant in its
contents. Both ``map`` and ``bind`` return new objects. Iterable.

### Functional tuple - `pythonic_fp.containers.functional_tuple` 

Subclassed tuple with a more functional interface. Gives tuple FP
methods. Designed to be further inherited from. Hashable if all
contained items are hashable.

### Immutable list - `pythonic_fp.containers.immutable_list`

A hashable, immutable, list-like data structure. Hashability will be
enforced when instantiated. Mutable list methods will return new
objects.

### Maybe monad - `pythonic_fp.containers.maybe`

An implementation of the maybe (or optional) monad. Data structure
represents a possibly missing value. Useful in implementing exception
free code paths.

### Either monad - `pythonic_fp.containers.xor`

An implementation of a left biased either monad. Data structure
representing either a "left" or "right" value, but not both. These two
values can be the same or different types. The "left" value is usually
taken to be the "happy path" of code flow. The "right" value is often
used for an error condition or a text string describing what went wrong.

This PyPI project is part of of the grscheller
[pythonic-fp namespace projects](https://grscheller.github.io/pythonic-fp/).

## Documentation

Documentation hosted on
[GitHub Pages](https://grscheller.github.io/pythonic-fp-containers/).

## Copyright and License

Copyright (c) 2023-2025 Geoffrey R. Scheller. Licensed under the Apache
License, Version 2.0. See the LICENSE file for details.
