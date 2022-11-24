import requests
from bs4 import BeautifulSoup
import json

result = requests.get("https://devgan.in/all_sections_ipc.php")
#model = SentenceTransformer('sentence-transformers/msmarco-distilbert-base-v4')
corpus = []
sections = dict()

soup = BeautifulSoup(result.content, 'lxml')
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
        if desc:
            sections["Section "+link.split('/')[-2]] = desc.text
            '''Use this data to make model'''
    except:
        print("Exception occurred.")

with open("section_dict.json", "w", encoding="utf-8") as file1:
    json.dump(sections, file1)

'''Making the model'''

# corpus_embedding = model.encode(corpus, convert_to_tensor=True, show_progress_bar=True, batch_size=32)
#
# query = ['X tried to stab Y to death using a knife, however Shyam was able to fend him off using a bat nearby which caused Ram to suffer a concussion and lose consciousness.']
# query_embedding = model.encode(query, convert_to_tensor=True)
#
# hits = util.semantic_search(query_embedding, corpus_embedding, top_k = 10)
#
# for hit in hits[0]:
#     print(corpus[hit['corpus_id']], 'Score: {:.4f}'.format(hit['score']))
