import requests
from bs4 import BeautifulSoup
import csv

# Fazer a requisição à página web
response = requests.get('Insert Link Here')

# Criar objeto BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

trem = soup.find_all('div', attrs={'role': 'presentation'})  # Encontra todas as DIVs com role="presentation"

episodes = trem
Arquivo = open('nomesEpsBrothersCast.csv', 'w', newline='', encoding='utf-8')
w = csv.writer(Arquivo)
w.writerow(['Data', 'Nome'])  # Cabeçalho do CSV

for i in range(0, len(episodes), 3):

    episode_i = episodes[i]
    episode_ii = episodes[i + 1]

    episode_texti = episode_i.get_text(strip=True)
    episode_textii = episode_ii.get_text(strip=True)

    DataEp = ''.join(episode_texti)
    NomeEp = ''.join(episode_textii)

    w.writerow([DataEp, NomeEp])  # Escreve os dados no CSV

Arquivo.close()
