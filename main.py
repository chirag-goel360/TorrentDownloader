from bs4 import BeautifulSoup
import urllib.request
import re
import os

files = open('DownloadList.txt', 'r')
notfoundfiles = open('NotFound.txt', 'a')
foundfiles = open('Found.txt', 'a')

for name in files:
  torrent = 'Not Available'   
  filename = name   
  name = name.strip()
  name = name.replace(" ","%20")
  name = "https://piratebay.party/search/" + name + "/1/99/0"
  html_page = urllib.request.urlopen(name)
  soup = BeautifulSoup(html_page, 'html.parser')
  for opentorrent in soup.findAll('a', attrs={'href': re.compile("^magnet:")}):
    torrent = opentorrent.get('href')
    break 
  if torrent != 'Not Available':
    os.startfile(torrent)
    print("Added to download", filename)
    foundfiles.write(filename)
  else:
    print("Not Added to download",filename)
    notfoundfiles.write(filename)
files.close()
notfoundfiles.close()
foundfiles.close()