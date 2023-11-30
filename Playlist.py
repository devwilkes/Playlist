# An initial file for the project.
from argparse import ArgumentParser
import json
import pandas as pd
import random
import re
import sys

class Song:
    """Represents a song that olds various musical properties.

    Attirbutes:
        title(str): The name of the Song.
        artist_names(list): The artist(s) that contributed in the Song.
        genre(str): The genre of music the Song fits.
        release_year(str): The year the Song was released.
        bpm(int): beats per minute (or tempo) of the Song.
    """

    def __init__(self, artists, album_name, track_name, popularity,
                 duration_ms, explicit, track_genre):
        """Initializes a Song object based on attached dataset's column names.

        Args:
            artists(str): the name of the artists involved in the song
            album_name(str): the name of the album the song is under
            track_name(str): the name of the song
            popularity(int): number between 0 and 100 that determines a song's popularity
            duration_ms(int): Track length in milliseconds
            explicit(bool): boolean value that determines if a song is explicit
            track_genre(str): the genre that the track belongs

        Side effects:
            Sets attributes for each argument.

        """
        
        self.artists = artists
        self.album_name = album_name
        self.track_name = track_name
        self.popularity = popularity
        self.duration_ms = duration_ms
        self.explicit = explicit
        self.track_genre = track_genre
        # Could possibly use some regex here, someone can tackle it
        
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

    def add_song(self):  # Ethan
        """Ask user if they want to add a song to the palylist by input the 
        information of the song.

        Args:
            song (str): a song
        """
        answer = input(
            "Do you want to add a song to your Playlist? Please answer 'yes' or 'no'")
        if answer == "yes":
            name = input("Please enter the name of the song")
            artists = input("Please enter the artist(s) of the song")
            genre = input("Please enter the genre of the song")
            release_year = input("Please enter the release year of the song")
            bpm = input("Please enter the bpm of the song")

            new_song = Song(name, artists, genre, release_year, bpm)
            self.song_list.append(new_song)
            print("Your song has been added to the Playlist!")
        else:
            print("No song will be add")

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

            "popularity": None,
            "duration": None,
            "explicit": None, # True or False or Unknown
            "danceability": None,
            "energy": None,
            "tempo": None,
            "genre": None,
            
        }

    # Sets the user's preferences for the playlist based on dataset column names
    def user_preferences(self, popularity=None,
                         duration=None, explicit=None, 
                         danceability=None, energy=None,
                         tempo = None, genre = None):

        self.preferences["popularity"] = popularity
        self.preferences["duration"] = duration
        self.preferences["explicit"] = explicit
        self.preferences["danceability"] = danceability
        self.preferences["energy"] = energy
        self.preferences["tempo"] = tempo
        self.preferences["genre"] = genre

# Justin
    def filtered_songs(self, criteria):
        """Filters the list of songs based on user-provided criteria

        Returns:
            A refined list of songs that match the user's criteria
        """
        filtered_results = []