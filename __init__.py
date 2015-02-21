# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup, Comment, NavigableString
import sys, codecs, json

class Track(object):
	def __init__(self,trackName,album,artist):
		self.name = trackName
		self.album = album
		self.artist = artist
	def __repr__(self):
		return self.name 
	def link(self):
		return 'http://lyrics.wikia.com/{0}:{1}'.format(self.artist.replace(' ', '-'),self.name.replace(' ','-'))
	def getLyrics(self):
		return PyLyrics.getLyrics(self.artist,self.name)
class Artist(object):
	def __init__(self, name):
		self.name = name 
	def getAlbums(self):
		return PyLyrics.getAlbums(self.name)
class Album(object):
	def __init__(self, name, link,singer):
		self.year = name.split(' ')[-1]
		self.name = name.replace(self.year,' ').rstrip()
		self.url = link 
		self.singer = singer
	def link(self):
		return self.url 
	def __repr__(self):
		return self.name
	def artist(self):
		return self.singer
class PyLyrics:
	@staticmethod
	def getAlbums(singer):
		singer = singer.replace(' ', '_')
		s = BeautifulSoup(requests.get('http://lyrics.wikia.com/{0}'.format(singer)).text)
		spans = s.findAll('span',{'class':'mw-headline'})
		albums = []
		for tag in spans:
			try:
				a = tag.findAll('a')[0]
				albums.append(Album(a.text,'http://lyrics.wikia.com' + a['href'],singer))
			except:
				pass
		return albums
	@staticmethod 
	def getTracks(album):
		if not isinstance(album, Album):
			raise TypeError("Parameter is not an instance of Album Class")
			return None
		url = "http://lyrics.wikia.com/api.php?artist={0}&fmt=xml".format(album.artist())
		soup = BeautifulSoup(requests.get(url).text)

		for al in soup.find_all('album'):
			if al.text == album.name:
				currentAlbum = al
				break
		songs =[Track(song.text,album,album.artist()) for song in currentAlbum.findNext('songs').findAll('item')]
		return songs

	@staticmethod
	def getLyrics(singer, song):
		#Replace spaces with _
		singer = singer.replace(' ', '_')
		song = song.replace(' ', '_')
		r = requests.get('http://lyrics.wikia.com/{0}:{1}'.format(singer,song))
		s = BeautifulSoup(r.text)
		#Get main lyrics holder
		lyrics = s.find("div",{'class':'lyricbox'})
		if lyrics is None:
			raise ValueError("Song or Singer does not exist")
			return None
		#Remove Scripts
		[s.extract() for s in lyrics('script')]

		#Remove Comments
		comments = lyrics.findAll(text=lambda text:isinstance(text, Comment))
		[comment.extract() for comment in comments]

		#Remove unecessary tags
		for tag in ['div','i','b','a']:
			for match in lyrics.findAll(tag):
				match.replaceWithChildren()
		#Get output as a string and remove non unicode characters and replace <br> with newlines
		output = str(lyrics).encode('utf-8')[22:-6:].decode("utf-8").replace('\n','').replace('<br/>','\n')
		try:
			return output
		except:
			return output.encode('utf-8')

album = PyLyrics.getAlbums('Taylor Swift')

tracks = PyLyrics.getTracks(album[-1])
print (tracks[1].getLyrics())

	