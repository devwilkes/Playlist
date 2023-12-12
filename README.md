# Playlist
A group final project for INST326 meant to showcase Python knowledge and skills, with a primary focus on managing data retrieved from databases.

Group Name: Function

Group Members: Lexin Deang, Pernelle De Souza, Justin Flores, Yihe Liu, Devon Wilkes

Song Data Source: https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset

Method Function | Primary Author | Techniques Demonstrated
:---: | :---: | :---:
parse_args() | *Devon Wilkes* | The ArgumentParser class from the argparse module
Playlist and Song Classes | *Lexin Deang* | Composition of two custom classes
remove_song() | *Yihe Liu* | Optional parameters
filter_songs() | *Justin Flores* | With statements
__str__() (Playlist class) | *Pernelle De Souza* | F-strings containing expressions
__repr__() (Song Class) | *Justin Flores* | Showcases a formal attribute of a class
generate_queue() | *Devon Wilkes* | Use of a key as a lambda expression using sorted()
__add__ (Playlist class) | *Lexin Deang* | Set operations
Filtering (Jupyter Notebook)| *Pernelle De Souza* | Filtering using Pandas DataFrames
Graphing (Jupyter Notebook) | *Yihe Liu* | Visualizing data with PyPlot/Seaborn

FILE DISTRIBUTION DESCRIPTIONS: 
**dataset.csv** - The dataset imported from Kaggle.com
**dataset.txt** - The dataset re-imported, changing delimiters into tab for easier regex.
**Final Project Table** - The final project contributions table
**Playlist_Analysis.ipynb** - A brief analysis of the dataset by kaggle
**Playlist.py** - Main Playlist


EXAMPLE COMMAND LINE ARG:
python Playlist.py Richard GymRatPlaylist 80 180000 True 'hip-hop'
