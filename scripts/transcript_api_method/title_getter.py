import requests
from bs4 import BeautifulSoup

def get_title(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")

    raw_title = soup.find_all(name="title")[0]

    title = raw_title.text
    title = title.replace(" - YouTube", "")

    return title

