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

ct = ssl.create_default_context()
ct.check_hostname = False
ct.verify_mode = ssl.CERT_NONE

req = Request(url, headers = {'User-Agent' : 'Chrome/77.0.3865.120' })
webpage = urlopen(req).read()

# print(webpage)

soup = BeautifulSoup(webpage, 'html.parser')
html = soup.prettify('utf-8')
song_json = {}
song_json["Lyrics"] = []
# song_json["Comments"] = []
# print(html)

for title in soup.findAll('title'):
    song_json["Title"] = title.text.strip()

for span in soup.findAll('span', attrs = {'class' : 'metadata_unit-info metadata_unit-info--text_only'}):
    song_json["Release Date"] = span.text.strip()

for div in soup.findAll('div', attrs = {'class': 'lyrics'}):
  song_json["Lyrics"].append(div.text.strip().split("\n"))

with open(song_json["Title"] + '.json', 'w') as outfile:
  json.dump(song_json, outfile, indent = 4, ensure_ascii = False)

print(song_json)
