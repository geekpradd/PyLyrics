import unittest
try:
	from .__init__ import * #Python 3
except:
	from __init__ import *

try:
	basestring = basestring
except NameError:
	basestring = (str, bytes)

albums = PyLyrics.getAlbums('Taylor Swift')
class PyLyricsTest(unittest.TestCase):
	def testAlbums(self):
		self.assertIsInstance(albums,list)
	def testTracks(self):
		self.assertIsInstance(albums[0].tracks(),list)
	def testLyrics(self):
		self.assertIsInstance(PyLyrics.getLyrics('Eminem','The Monster'),basestring)

if __name__=='__main__':
	unittest.main()