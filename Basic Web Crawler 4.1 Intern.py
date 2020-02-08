from bs4 import BeautifulSoup
import requests
import json

url_naweb = 'https://theinternship.io'
r = requests.get(url_naweb)
r.encoding = 'utf-8'

if r.ok:
    tag= BeautifulSoup(r.text,"html.parser").find_all("div",{"class": "partner","data-v-018ba4ef": ""})
    arrange = {}
    for i in tag:
        arrange.update({len(i.span.getText()):(i.img.get("src"))})
    for j in sorted(arrange):
        print(arrange[j])
