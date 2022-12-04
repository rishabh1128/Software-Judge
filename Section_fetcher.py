import requests
from bs4 import BeautifulSoup
import json

result = requests.get("https://devgan.in/all_sections_ipc.php")

corpus = []
sections = dict()

soup = BeautifulSoup(result.content, "lxml")
links = soup.find_all("a")
section_links = []

for link in links:
    if link.attrs.get('href') and link.attrs.get('href').startswith('/ipc'):
        section_links.append(link.attrs.get('href'))

links = section_links

for link in links:
    try:
        section = requests.get("https://devgan.in"+link)
        soup = BeautifulSoup(section.content, 'lxml')
        desc = soup.find('tr', class_='mys-desc')
        if desc and "shall be punished" in desc.text:
            sections["Section "+link.split('/')[-2]] = desc.text
            '''Use this data to make model'''
    except:
        print("Exception occurred.")

with open("section_dict.json", "w", encoding="utf-8") as file1:
    json.dump(sections, file1)





