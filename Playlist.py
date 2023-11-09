# An initial file for the project.
from argparse import ArgumentParser
import pandas as pd
import re
import sys

# Dictionary of genres and their corresponding BPM ranges
# Citation: https://www.fatpick.com/blog/glossary-tempo
GENRE = {
    
   "R&B" : [60, 80], 
   "Reggae" : [60, 90],
   "Hip Hop" : [70, 100],
   "Dubstep" : [80, 90],
   "Pop" : [100, 130],
   "Country" : [108, 148], 
   "Rock" : [110, 140], 
   "Metal" : [128, 160]
    
    
}
class Song:
    """Represents a song in the playlist.
    """

    def __init__(self):
        """Initializes a Song object."""

    def filtered_songs(self, criteria):
        """Filters the list of songs based on user-provided criteria

        Returns:
            A refined list of songs that match the user's criteria
        """
        filtered_results = []
        

class Playlist:
    """Represents a playlist of songs.
    """

    def __init__(self):
        """Initializes a Playlist object."""

    def generate_queue(self):
        """ Creates a queue of songs to be played by the user. Can be generated
        randomly or generated with user criteria.
        """

    def add_song(self, song):
        """allows user to add songs

        Args:
            song (str): a song
        """
    def sort_by_popularity(self, ascending=True):
        """ This method can sort the songs by popularity
        """
        
class User:
    """ A class for users with playlists
    """
    
    def __init__(self, username): 
        self.name = username
        self.playlist = Playlist()
        # A dict of the user's preferences for the playlist
        self.preferences = {
            
            "genre" : None,
            "streams" : None,
            "bpm" : None,
            "key" : None
            
        }
        
    # Sets the user's preferences for the playlist based on genre and bpm
    def user_preferences(self, genre = None, 
                         streams = None, bpm = None, key = None):
        
        pass
        


