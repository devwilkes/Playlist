# An initial file for the project.
from argparse import ArgumentParser
import json
import pandas as pd
import random
import re
import sys

# Dictionary of genres and their corresponding BPM ranges
# Citation: https://www.fatpick.com/blog/glossary-tempo

# Lexin
GENRE = {

    "R&B": [60, 80],
    "Reggae": [60, 90],
    "Hip Hop": [70, 100],
    "Dubstep": [80, 90],
    "Pop": [100, 130],
    "Country": [108, 148],
    "Rock": [110, 140],
    "Metal": [128, 160]
}


class Song:
    """Represents a song that olds various musical properties.

    Attirbutes:
        title(str): The name of the Song.
        artist_names(list): The artist(s) that contributed in the Song.
        genre(str): The genre of music the Song fits.
        release_year(str): The year the Song was released.
        bpm(int): beats per minute (or tempo) of the Song.
    """

    def __init__(self, name, artist_names, genre, release_year, bpm):
        """Initializes a Song object.

        Args:
            title(str): The name of the song.
            artist_names(list): The artist(s) who worked on the Song.
            genre(str): The grenre of music the Song fits.
            release_year(str): The year the Song was released.
            bpm(int): beats per minute (or tempo) of the Song.

        Side effects:
            Sets attributes for 'title', 'atrist_names', 'genre', 
            'release_year', and 'bpm'.

        """
        # Could possibly use some regex here, someone can tackle it

        self.name = name
        self.artist_names = artist_names
        self.genre = genre
        self.release_year = release_year
        self.bpm = bpm

# Justin
    def filtered_songs(self, criteria):
        """Filters the list of songs based on user-provided criteria

        Returns:
            A refined list of songs that match the user's criteria
        """
        filtered_results = []


class Playlist:
    """Represents a playlist of songs.

    Attributes:
        song_list(list): a list containing Song objects present in the Playlist.
    """

    def __init__(self):
        """Initializes a Playlist object.

        Args:
            song_list(list): A list of Songs present in the Playlist.

        Side effects: Sets attributes for 'song_list'.
        """
        self.song_list = []

    def generate_queue(self, criteria=None, value=None):  # Devon
        """ Creates a queue of songs from the Playlist to be played by 
        the user. Can be generated randomly or sorted with user criteria and 
        values for that criteria.

        Args:
            criteria(str): A filter that filters the generated queue based on 
            properties of a Song such as bpm or artist. Defaults to None.
            value(str): A value of a criteria to filter a queue even further. 
            Can only be used with a valid criteria parameter. Defaults to None.

        Returns:
            list(Song): The generated queue of Songs.
        """
        queue = []

        if (criteria is not None and value is not None):
            # Will add functionality to only include songs that match the attribute given in criteria and value
            queue = [song for song in self.song_list]
        elif (criteria is not None and value is None):
            # Will add cunctionality to only include songs that match the attribute given in criteria
            queue = sorted(self.song_list)
        elif (criteria is None and value is not None):
            raise ValueError()
        else:
            queue.shuffle(self.song_list)
        return queue

    def add_song(self, name, artists, genre, release_year, bpm):  # Ethan
        """Ask user if they want to add a song to the palylist by input the 
        information of the song.

        Args:
            name (str): The name of the song.
            artists (list): The artist(s) of the song.
            genre (str): The genre of the song.
            release_year (str): The release year of the song.
            bpm (int): Beats per minute of the song.
        """        
        if any(song.name == name for song in self.song_list):
            print("Your song exists in the Playlist, no song will be add")
        else:
            new_song = Song(name, artists, genre, release_year, bpm)
            self.song_list.append(new_song)               
            print("Your song has been added to the Playlist!")
                

    def sort_by_popularity(self, ascending=True):
        """ This method can sort the songs by popularity
        Args:
            ascending (bool): If True, sort in ascending order; otherwise, sort in decending order,
        """
        # Sorting the songs based on the populairty attribute of each songs
        self.songs.sort(key=lambda song: song.popularity,
                        reverse=not ascending)

# Lexin


class User:
    """ A class for users with playlists
    """

    def __init__(self, username):
        self.name = username
        self.playlist = Playlist()

        # A dict of the user's preferences for the playlist
        self.preferences = {

            "genre": None,
            "streams": None,
            "bpm": None,
            "key": None

        }

    # Sets the user's preferences for the playlist based on genre and bpm
    def user_preferences(self, genre=None,
                         streams=None, bpm=None, key=None):

        self.preferences["genre"] = genre
        self.preferences["streams"] = streams
        self.preferences["bpm"] = bpm
        self.preferences["key"] = key

        pass
