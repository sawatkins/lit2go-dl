import requests
import os
from bs4 import BeautifulSoup

def make_dir(path):
    try:
        os.makedirs(path)
    except OSError:
        pass
    print("Created directory", path)
    os.chdir(path)

def download_mp3(mp3_link, filename):
    doc = requests.get(mp3_link)
    with open(filename, 'wb') as f:
        print("Downloading", filename)
        f.write(doc.content)

def get_mp3_link(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    for link in soup.find_all('source'):
        if link is not None:
            # Why the fuck arent the ogg file getting here!?
            return link.get('src')

base_url = input("Enter url of book from lit2go site: ")
#test_base_url = "https://etc.usf.edu/lit2go/21/the-adventures-of-huckleberry-finn"
book_name = base_url.strip('/').split('/')[-1]
print("Found audiobook:", book_name)
make_dir("./" + book_name)

r = requests.get(base_url)
soup = BeautifulSoup(r.content, "html.parser")
for link in soup.find_all('a'):
    if link.get('href'):
        actual_link = link.get('href')
    if book_name in actual_link:
        #print("actual_link:", actual_link)
        mp3_link = get_mp3_link(actual_link)
        #print("mp3_link:", mp3_link)
        filename = actual_link.strip('/').split('/')[-1] + ".mp3"
        download_mp3(mp3_link, filename)


