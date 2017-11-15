
backtrader_contrib
==================

.. image:: https://img.shields.io/pypi/v/backtrader.svg
   :alt: PyPi Version
   :scale: 100%
   :target: https://pypi.python.org/pypi/backtrader_contrib/

.. image:: https://img.shields.io/pypi/pyversions/backtrader.svg
   :alt: Python versions
   :scale: 100%
   :target: https://pypi.python.org/pypi/backtrader_contrib/

Features:
=========

This is the repostory for foreign contributions to ``backtrader``.

Pull Requests can be accepted with the following LICENSES:

  - GPLv3
  - MIT
  - BSD 3-Clause
  - Apache 2.0

How does it work
================

The package will scan ``.py`` file inside the corresponding subpackages (like
``analyzers``, ``indicators``, etc) and will import the classes which are
subclasses of the corresponding subpackages (``Analyzer``, ``Indicator``)

Errors will be silently ignored

Successfully imported elements will be added to the corresponding subpackage of
``backtrader``. I.e.: anything inside ``backtrader_contrib.indicators`` will be
monkey-patched (added) to ``backtrader.indicators``

The package will auto-replace itself and return ``backtrader``

Usage
=====

As simple as::

  import backtrader_contrib as bt

And carry on using ``bt`` as if you had directly imported *backtrader*
