import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json
import ast
import os

from urllib.request import Request, urlopen

from getUrl import url

#For ignoring SSL certificate errors
ct = ssl.create_default_context()
ct.check_hostname = False
ct.verify_mode = ssl.CERT_NONE

#Making the website believe that you are accessing it using a browser
req = Request(url, headers = {'User-Agent' : 'Chrome/77.0.3865.120' })
webpage = urlopen(req).read()

# print(webpage)

#Creating a BeautifulSoup object of the html page for extraction of data
soup = BeautifulSoup(webpage, 'html.parser')
html = soup.prettify('utf-8')
song_json = {}
song_json["Lyrics"] = []
song_json["Comments"] = []
# print(html)

#Extract Title of the song
for title in soup.findAll('title'):
    song_json["Title"] = title.text.strip()

#Extract the release date of the song
for span in soup.findAll('span', attrs = {'class' : 'metadata_unit-info metadata_unit-info--text_only'}):
    song_json["Release Date"] = span.text.strip()


#Extract the Lyrics of the song
for div in soup.findAll('div', attrs = {'class': 'lyrics'}):
  song_json["Lyrics"].append(div.text.strip().split("\n"))

#Extract the Comments on the song
for div in soup.findAll('div', attrs = {'class': 'rich_text_formatting'}):
  comments = div.text.strip().split("\n")
  for comment in comments:
      if comment != " ":
          song_json["Comments"].append(comment)

#Save the json created with the file name as title + .json
with open(song_json["Title"] + '.json', 'w') as outfile:
  json.dump(song_json, outfile, indent = 4, ensure_ascii = False)

# print(song_json)

print('----------Extraction of data is complete. Check json file.----------')
