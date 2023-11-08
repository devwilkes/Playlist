# An initial file for the project.
from argparse import ArgumentParser
import pandas as pd
import re
import sys


class Song:
    """Represents a song in the playlist.
    """

    def __init__(self):
        """Initializes a Song object."""

    def filtered_songs(self):
        """Filters the list of songs based on user-provided criteria

        Returns:
            A refined list of songs that match the user's criteria
        """


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


class Sort:
    """ A class for sorting songs in the playlist by popularity 
    """

    def __init__(self, songs):
        """
        initialize the sort class with a list of songs 

        the args- songs list - a list of song dictionaries with 'name' and 
        'popularity' attributes
        """

    def sort_by_popularity(self, ascending=True):
        """
        sorting the songs by popularity in ascending or descending order 

        the args- set to true for ascending , false for descending, default will be true 
        """
