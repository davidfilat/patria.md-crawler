import requests
from bs4 import BeautifulSoup


def clean_me(html):
    soup = BeautifulSoup(html, 'html.parser')
    for s in soup(['script', 'style']):
        s.decompose()
    return soup


url = 'https://patria.md/movies/gogol-razbunare-grozava/'
r = requests.get(url)
if r.status_code >= 200:
    soup = clean_me(r.text)
    html = soup.prettify("utf-8")
with open("output.html", "wb") as file:
    file.write(html)
