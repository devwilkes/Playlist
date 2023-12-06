# An initial file for the project.
from argparse import ArgumentParser
from itertools import islice
import json
import random
import re
import sys


class Song:
    """Represents a song that olds various musical properties.

    Attirbutes:
        artists(str): the artists involved in the song
        track_name(str): the name of the song

        popularity(int): the rating of popularity based on the dataset
        duration_ms(int): how long the song is in milliseconds
        explicit(bool): if the song is explicit or not
        track_genre(str): The genre that the song belongs in.
        album_name(str): the name of the album the song is under

    """

    def __init__(self, artists, track_name):
        """Initializes a Song object based on attached dataset's column names.

        Args:
            artists(str): the artists involved in the song
            album_name(str): the name of the album the song is under
            track_name(str): the name of the song


        Side effects:
            Sets attributes for each argument.

        """

        self.artists = artists
        self.track_name = track_name

        # filterable properties
        self.properties = {
            "popularity": 0,
            "duration": 0,
            "explicit": False,
            "genre": '',
            "album_name": ''
        }

    def __str__(self):
        """Returns an informal string representation of the song,

        Returns:
            str: An informal representation of the song.
        """
        return f"'{self.track_name}' by {self.artists}"

    def __repr__(self):
        """Returns a formal string representation for the song.

        Returns:
            str: A formal string representation of the song.
        """
        return f"Song({(self.track_name)}, {(self.artists)})\n{self.properties}\n"


class Playlist:
    """Represents a playlist of songs.

    Attributes:
        song_list(list): a list containing Song objects present in the Playlist.
        name(str): the name of the playlist (default: "Playlist")
    """

    def __init__(self):
        """Initializes a Playlist object.

        Args:
            song_list(list): A list of Songs present in the Playlist.

        Side effects:
            Sets attributes for 'song_list' and 'name'.
        """
        self.song_list = []
        self.name = "Playlist"

    def __str__(self):
        """ Returns an informal string representation of the playlist

        Returns:
            str: A string representation of the playlist.
        """

        playlist = f"Playlist {self.name} : \n"
        for song in self.song_list:
            playlist += f"'{song.track_name}' by {song.artists}\n"

        return playlist

    def __repr__(self):
        """ Returns a formal string representation of the playlist
        """
        playlist = f'Playlist {self.name}: \n'
        for song in self.song_list:
            playlist += f'\n'
            playlist += f"*****'{song.track_name}' by {song.artists}*****\n"
            playlist += "{\n"
            for key, value in song.properties.items():
                playlist += f"{key}: {value},\n "
            playlist += "}\n"

        return playlist

    def __add__(self, other):
        """ Adds two playlists together

        Returns:
            list: A list of songs that are in both playlists.
        """
        new = set(self.song_list) | set(other.song_list)
        new_playlist = Playlist()
        new_playlist.song_list = list(new)
        return new_playlist

    def add_name(self, user_name):  # Devon
        """ Updates the name for the Playlist with a user input.

        Side effects: 
            Updates the value of 'name'.
        """
        self.name = user_name

    def add_song(self, song=None, artists=None, track_name=None):
        """
        Adds a song to the playlist

        Args:
            song (obj): the existing song
            artists (str): the artists involved in the song
            track_name (str): the name of the song
        """
        if song is None and artists is None and track_name is None:
            raise ValueError("No values inputted (song, artists, track_name)")
        existing_songs = [song.track_name for song in self.song_list]
        if track_name in existing_songs:
            print(f"The song '{track_name}' already exists in {self.name}.")
        else:
            if artists is not None and track_name is not None:
                new_song = Song(artists, track_name)
                self.song_list.append(new_song)
                print(f"Your song has been added to {self.name}!")
            elif song is not None:
                self.song_list.append(song)

    def remove_song(self, song=None, artists=None, track_name=None, ):
        """
        Removes a song from the Playlist

        Args:
            artists (str): the artists involved in the song
            song (obj): the existing song
            track_name (str): the name of the song

        Raises:
            ValueError: If the song is not in the Playlist
        """
        if song is None and artists is None and track_name is None:
            raise ValueError("No values inputted (song, artists, track_name)")
        existing_songs = [song.track_name for song in self.song_list]
        if track_name in existing_songs:
            if song is not None:
                song = Song(artists, track_name)
                self.song_list.remove(song)
                print(f"'{track_name}' have been removed from {self.name}!")
            else:
                self.song_list.remove(song)
        else:
            raise ValueError("The song is not in the Playlist!")

    def sort_by_popularity(self, ascending=True):
        """ This method can sort the songs by popularity
        Args:
            ascending (bool): If True, sort in ascending order; 
                                otherwise, sort in decending order,

        Side effects:
            Sorts the 'song_list' attribute.
        """
        # Sorting the songs based on the populairty attribute of each songs
        self.song_list.sort(key=lambda song: song.properties.get('popularity'),
                            reverse=not ascending)


def matches_preferences(user, song):
    """Checks if a song matches the user's preferences

    Args:
        song (Song): A song object

    Returns:
        bool: True if the song matches the user's preferences, False otherwise
    """
    for key, value in user.preferences.items():
        if value is not None:
            if key == "explicit":
                if song.properties[key] != value:
                    return False
            elif key == "genre":
                if song.properties[key] != value:
                    return False
            elif key == "duration":
                if song.properties[key] > value:
                    return False
            elif key == "popularity":
                if song.properties[key] < value:
                    return False
    return True


class User:
    """ A class for users with playlists.

    Attributes:
        preferences (dict): A dictionary containing user preferences for the playlist
        playlist (Playlist): The user's playlist
        name (str): The username
    """

    def __init__(self, username):
        """Initialize a User object

        Args:
            username (str): The username for the user.

        Side effects:
            Initializes 'name' and 'playlist' attributes.
            Initializes 'preferances' dictionary with default values.
        """
        self.name = username
        self.playlist = Playlist()
        self.queue = []

        # A dict of the user's preferences for the playlist
        self.preferences = {

            "popularity": None,
            "duration": None,
            "explicit": None,  # True or False or Unknown
            "genre": None,

        }

    # Sets the user's preferences for the playlist based on dataset column names
    def user_preferences(self, popularity=None,
                         duration=None, explicit=None,
                         genre=None):
        """Set the user's preferences for the playlist

        Args:
            popularity (int, optional): The popularity rating threshold. Defaults to None.
            duration (int, optional): The maximum duration of songs in milliseconds. Defaults to None.
            explicit (bool, optional): Specifies if explicit. Defaults to None.
            genre (str, optional): The preferred genre. Defaults to None.
        """

        self.preferences["popularity"] = popularity
        self.preferences["duration"] = duration
        self.preferences["explicit"] = explicit
        self.preferences["genre"] = genre

    def filter_songs(self):
        """Filters the list of songs based on user-provided criteria

        Returns:
            A refined list of songs that match the user's criteria
        """

        filtered_results = []
        pattern = r'''(?x)^(\d+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t
                        (\d+)\t(\d+)\t(FALSE|TRUE)\t([\d.]+)\t(.+?)\t(\d+)\t
                        ([-.\d]+)\t(\d+)\t([\d.]+)\t(.+?)\t(.+?)\t([\d.]+)\t
                        (.+?)\t([\d.]+)\t(\d+)\t([^\t]+)$'''

        with open("dataset.txt", encoding='utf-8') as file:

            for line in islice(file, 1, None):
                match = re.search(pattern, line.strip())
                artists, track_name = match.group(3), match.group(5)
                song = Song(artists, track_name)

                song.properties['popularity'] = int(match.group(6))
                song.properties['duration'] = int(match.group(7))
                song.properties['explicit'] = bool(match.group(8))
                song.properties['genre'] = match.group(21)
                song.properties['album_name'] = match.group(4)

                if matches_preferences(self, song):
                    filtered_results.append(song)

        for song in filtered_results:
            self.playlist.add_song(song)

    def generate_queue(self, preference=None, length=10, rev=False):
        """ Creates a queue of Songs within the User's playlist to be played. 
        The order of these songs is shuffled by default, but can be sorted, 
        reversed, and specified with a certain length.

        Args:
            preference(str): A preference to sort the queue by. 
            Defaults to None.
            length(int): A length specifier for the queue. Defaults to 10.
            reverse(bool): Reverses the order of the newly sorted/shuffled 
            songs. Defaults to False.

        Side effects:
            Updates the value of 'queue'.
        """
        temp_queue = []
        if (preference is not None):
            temp_queue = sorted(self.playlist.song_list, key=lambda s: s.properties.get(
                preference), reverse=rev)
        else:
            temp_queue = random.sample(
                self.playlist.song_list, len(self.playlist.song_list))
        counter = 0
        while counter < length:
            self.queue.append(temp_queue.pop(0))

    def play_button(self):
        """ 'Plays' a song from the top of the queue. Displays the song that's
        currently playing as well as what's next in the queue.

        Returns:
            str: A visualization of the song playing and the songs currently 
            in queue.

        Side effects:
            Updates the value of 'queue'.
        """
        playing = f"Now Playing from {self.playlist.name}: {self.queue[0]}\n"
        self.queue[0].pop
        playing += f"Up next: {self.queue[0]}"
        playing += "In queue: \n"
        counter = 1
        while counter < len(self.queue):
            playing += f"{self.queue[counter]} \n"
        return playing


# Might change later to involve a JSON file instead of parameters for preferences
def main(name, playlist_name, popularity, duration, explicit, genre):
    """The main function of the program.

    Args:
        name(str): The name of a User.
        playlist_name(str): The name of a Playlist
        popularity(str): The user's preferred popularity
        duration(str): The user's preferred song duration
        explicit(str): The user's preferred explicit filter
        genre(str): The user's preferred music genre

    Side effects:
        Prints out the results of the program.
    """
    print(f'--USER CREATED : {name}')
    print(f'--PLAYLIST CREATED : {playlist_name}')
    print('-' * 100 + '\n')
    user = User(name)
    user.playlist.add_name(playlist_name)
    user.preferences["popularity"] = int(
        popularity) if popularity.lower() != 'none' else None
    user.preferences["duration"] = int(
        duration) if duration.lower() != 'none' else None
    user.preferences["explicit"] = explicit.lower(
    ) != 'none' and explicit.lower() == 'true'
    user.preferences["genre"] = genre if genre.lower() != 'none' else None
    print(f'--USER PREFERENCES : {str(user.preferences)}\n')
    print('-' * 100 + '\n')

    print(f'--FILTERING SONGS BASED ON USER PREFERENCES')
    print('-' * 100 + '\n')
    user.filter_songs()

    print(user.playlist)

    print('-' * 100 + '\n')
    print(f'--SORTING SONGS BY POPULARITY\n')
    user.playlist.sort_by_popularity()

    print(repr(user.playlist))


def parse_args(arglist):
    """ Parses command-line arguments

    Args:
        arglist (list): a list of command-line arguments.

    Returns:
        args (argparse): The parsed command-line arguments. 
    """
    parser = ArgumentParser()
    parser.add_argument("name", help="The user using the Playlist function")
    parser.add_argument("playlist_name", help="The name of the playlist")
    parser.add_argument("popularity", help="The user's preferred popularity")
    parser.add_argument("duration", help="The user's preferred song duration")
    parser.add_argument(
        "explicit", help="The user's preferred explicit filter")
    parser.add_argument("genre", help="The user's preferred music genre")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.name, args.playlist_name, args.popularity,
         args.duration, args.explicit, args.genre)
