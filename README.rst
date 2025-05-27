========================
Pythonic FP - Containers
========================

Container based data structure, part of the
`PyPI pythonic-fp Namespace Projects <https://github.com/grscheller/pythonic-fp/blob/main/README.md>`_.

Repositories:
-------------

- `pythonic-fp.containers <https://pypi.org/project/pythonic-fp.containers>`_ project on *PyPI*
- `Source code <https://github.com/grscheller/pythonic-fp-containers>`_ on *GitHub*.

Detailed documentation:
-----------------------

Detailed API
`documentation <https://grscheller.github.io/pythonic-fp/maintained/containers>`_
on *GH-Pages*.

Features:
---------

Single item box - dtools.containers.box
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Container holding at most one object of a given type. This stateful
(mutable) container can contain only 0 or 1 items. Invariant in its
contents. Both ``map`` and ``bind`` return new objects. Iterable.

Functional tuple - dtools.containers.functional_tuple 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Subclassed tuple with a more functional interface. Gives tuple FP
methods. Designed to be further inherited from. Hashable if all
contained items are hashable.

Immutable list - dtools.containers.immutable_list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A hashable, immutable, list-like data structure. Hashability will be
enforced when instantiated. Mutable list methods will return new
objects.

Maybe monad - dtools.containers.maybe
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An implementation of the maybe (or optional) monad. Data structure
represents a possibly missing value. Useful in implementing exception
free code paths.

Either monad - dtools.containers.xor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An implementation of a left biased either monad. Data structure
representing either a "left" or "right" value, but not both. These two
values can be the same or different types. The "left" value is usually
taken to be the "happy path" of code flow. The "right" value is often
used for an error condition or a text string describing what went wrong.

Installation:
-------------

| $ pip install pythonic-fp.containers

Support:
--------

If you have any questions or issues with the software, feel free to reach out
to the maintainer at geoffrey@scheller.com, or submit an issue on GitHub's issue
tracker.

Contribute
^^^^^^^^^^

- Issue Tracker: https://github.com/grscheller/pythonic-fp-containers/issues
- Pull Requests: https://github.com/grscheller/pythonic-fp-containers/pulls

Contributers
^^^^^^^^^^^^

- `@grscheller <https://github.com/grscheller>`_ (Geoffrey R. Scheller - maintainer)

CHANGELOG
^^^^^^^^^

See the `CHANGELOG <https://github.com/grscheller/pythonic-fp-containers/blob/main/CHANGELOG.rst>`_

License:
--------

This project is licensed under the Apache License Version 2.0, January 2004.
See the `LICENCE file <https://github.com/grscheller/pythonic-fp-containers/blob/main/LICENSE>`_
for details.
