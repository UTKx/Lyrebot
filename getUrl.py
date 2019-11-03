import requests
from bs4 import BeautifulSoup

# Enter the desired Song Name
song_name = input("Enter the song name (Eg. Artist name song name): ")
lyrics = "-lyrics"

# Conversion to URL
raw_song_name = song_name.replace(" ", "-")

#  URL for the desired song
url_song_name = raw_song_name + lyrics

# Final URL
url = f"https://genius.com/{url_song_name}"

# Extraction of the data
res = requests.get(url)
src = res.content

# Parsing data using html parser
soup = BeautifulSoup(src, "html.parser")

# print(soup.prettify)