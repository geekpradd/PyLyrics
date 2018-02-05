## PyLyrics: A Pythonic Implementation of lyrics.wikia.com

[![Build Status](http://img.shields.io/travis/geekpradd/PyLyrics/master.svg?style=flat-square)](https://travis-ci.org/geekpradd/PyLyrics)
[![Latest Version](http://img.shields.io/pypi/v/PyLyrics.svg?style=flat-square)](https://pypi.python.org/pypi/PyLyrics/)
[![License](https://img.shields.io/pypi/l/PyLyrics.svg?style=flat-square)](https://pypi.python.org/pypi/PyLyrics/)

PyLyrics is a python module to get Lyrics of songs from lyrics.wikia.com. It has support for getting albums of a singer and songs from an album from which lyrics can be accessed.

### Installation

Installation is done using pip.

```
pip install PyLyrics
```

### Usage

PyLyrics provides various lyrics.wikia.com methods by using many layers of Abstraction. Firstly there are 3 core classes which define most of the return values of PyLyrics:

1. Track: Returned in Album Track searches and contains methods to get lyrics of the track
2. Album: Returned from Artist album searches and contains methods to get tracks
3. Artist: Returned from Artist searches and contains methods to get Albums

Some examples are shown below on usage:

##### Search for a Artist and list Albums

```python
from PyLyrics import *

albums = PyLyrics.getAlbums(singer='Eminem')
for a in albums:
	print (a) #Each album printed is a Album Object
```

##### List all tracks of an Album

You need to pass a Album Object into the function. This step is required to prevent errors and to ensure result

```python
from PyLyrics import *

albums = PyLyrics.getAlbums(singer='Eminem')
myalbum = albums[4] #Select your album based on Index

tracks = myalbum.tracks() #or PyLyrics.getTracks(myalbum)
for track in tracks:
	print (track) #Each track is a track object
	print (track.getLyrics()) #Get the lyrics
```
##### Get Lyrics of a song

There are two ways to do this. Either you can pass the name of the singer and the song name to the main function or use the bound method `getLyrics()` of the track object received as shown  in the previous example.

```python
from PyLyrics import *

print(PyLyrics.getLyrics('Taylor Swift','Blank Space')) #Print the lyrics directly
```
### Version 1.1 

Fixed a lot encoding errors and inconsistency

### About

Created by Pradipta (geekpradd), Copyright 2015.
