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
        artists(str): the artists involved in the song
        album_name(str): the name of the album the song is under
        track_name(str): the name of the song

        _popularity(int): the rating of popularity based on the dataset
        _duration_ms(int): how long the song is in milliseconds
        _explicit(bool): if the song is explicit or not
        _tempo(int): the song's tempo
        _track_genre(str): The genre that the song belongs in.
    """

    def __init__(self, artists, album_name, track_name):
        """Initializes a Song object based on attached dataset's column names.

        Args:
            artists(str): the artists involved in the song
            album_name(str): the name of the album the song is under
            track_name(str): the name of the song


        Side effects:
            Sets attributes for each argument.

        """

        self.artists = artists
        self.album_name = album_name
        self.track_name = track_name

        # filterable properties
        self._popularity = 0
        self._duration_ms = 0
        self._explicit = False
        self._tempo = 0
        self._track_genre = ''

    def __str__ (self):
        """Returns an informal string representation of the song.
        
        """
        return f"{self.track_name} by {self.artists}"
    
    def __repr__ (self):
        """Returns a formal string representation fo the song.

        """
        return f"Song({repr(self.track_name)}, {repr(self.artists)})"
    
song_instance = Song("Daniel Caesar", "Album Name", "Valentina")
print(str(song_instance))

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

    # Someone Implement These
    def __str__(self):
        """ Returns an informal string representation of the playlist
        """
        pass

    def __repr__(self):
        """ Returns a formal string representation of the playlist
        """
        pass

    def __add__(self, other):
        """ Adds two playlists together
        """
        pass

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
            raise ValueError(
                "You need a specific property before requesting a value!")
        else:
            queue.shuffle(self.song_list)
        return queue

    def generate_name(self):  # Devon
        """ Generates a name for the Playlist based off of the shared 
        properties of Songs in the Playlist.

        """

    def add_song(self, artists, album_name, track_name): #Ethan
        """
        Ask user if they want to add a song to the palylist by input the 
        information of the song.

        Args:
            artists (str): the artists involved in the song
            album_name (str): the name of the album the song is under
            track_name (str): the name of the song
        """
        existing_songs = [song.track_name for song in self.song_list]
        if track_name in existing_songs:
            print(f"The song '{track_name}' already exists in the playlist.")
        else:
            new_song = Song(artists, album_name, track_name)
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

            "popularity": None,
            "duration": None,
            "explicit": None,  # True or False or Unknown
            "danceability": None,
            "energy": None,
            "tempo": None,
            "genre": None,

        }

    # Sets the user's preferences for the playlist based on dataset column names
    def user_preferences(self, popularity=None,
                         duration=None, explicit=None,
                         danceability=None, energy=None,
                         tempo=None, genre=None):

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


def main(file_path):
    """ Reads from a file and generates Songs.

    Args: file_path (str): The path to the file containing raw text data.
    """


def parse_args(arglist):
    """ Parses command-line arguments

    Args:
        arglist (list): a list of command-line arguments.
    """
    parser = ArgumentParser()


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main()
