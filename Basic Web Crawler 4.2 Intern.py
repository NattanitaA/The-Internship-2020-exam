from bs4 import BeautifulSoup
import requests
import json

url_naweb = 'https://theinternship.io'
r = requests.get(url_naweb)
r.encoding = 'utf-8'

if r.ok:
    tag= BeautifulSoup(r.text,"html.parser").find_all('img')
    op = {"companies": [
                    {"logo": url_naweb + i.get("src")}
                        for i in tag if "company" in i.get("src")]}

with open("outputt.json","w+") as file:
    file.write(json.dumps(op))


