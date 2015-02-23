#Classes for Scrapers
try:
	from .functions import *
except:
	from functions import *
class Track(object):
	def __init__(self,trackName,album,artist):
		self.name = trackName
		self.album = album
		self.artist = artist
	def __repr__(self):
		return self.name.encode('utf-8')
	def link(self):
		return 'http://lyrics.wikia.com/{0}:{1}'.format(self.artist.replace(' ', '-'),self.name.replace(' ','-'))
	def getLyrics(self):
		return PyLyrics.getLyrics(self.artist,self.name)
class Artist(object):
	def __init__(self, name):
		self.name = name 
	def getAlbums(self):
		return PyLyrics.getAlbums(self.name)
	def __repr__(self):
		return self.name.encode('utf-8')
class Album(object):
	def __init__(self, name, link,singer):
		self.year = name.split(' ')[-1]
		self.name = name.replace(self.year,' ').rstrip()
		self.url = link 
		self.singer = singer
	def link(self):
		return self.url 
	def __repr__(self):
		return self.name.encode('utf-8')
	def artist(self):
		return self.singer
	def tracks(self):
		return PyLyrics.getTracks(self)