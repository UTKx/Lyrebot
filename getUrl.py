import requests
from bs4 import BeautifulSoup

song_name = input("Enter the song name (Eg. Artist name song name): ")
lyrics = "-lyrics"

raw_song_name = song_name.replace(" ", "-")

url_song_name = raw_song_name + lyrics

url = f"https://genius.com/{url_song_name}"

res = requests.get(url)
src = res.content

soup = BeautifulSoup(src, "html.parser")

print(soup.prettify)