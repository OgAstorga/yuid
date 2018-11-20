yuid
====

Introduction
------------

This is a simple script that generates a 64bit UUID and encodes it in base62 thus generating a secure unique 11 char string that are similar to the beloved youtube video ids


Structure
---------

Our 64 bit string is composed with the following method

10 bits are random
12 bits are a hash from machine id
42 bits are unixtime till milliseconds

they are all concatenated in the mentioned order


Install
-------

```
pip install yuid
```

Usage
-----

```
>>> from yuid import yuid
>>> yuid()
UAfxKExKjVQ
```
