# -- coding: utf-8 --

class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song("Happy birthday to you")

happy_bday.sing_a_song()
