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

print(webpage)