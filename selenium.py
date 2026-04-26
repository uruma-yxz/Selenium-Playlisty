import os
from selenium import webdriver
from selenium.webdriver.common.by import By

BuscaPlay = input('Colocar sua Playlist: ')

url = BuscaPlay
drive = webdriver.Chrome()
drive.get(url)
# limit = 
n = 1
linkAulas = []

while True:
    try:
        link = drive.find_element(By.XPATH,f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-playlist-video-list-renderer/div[3]/ytd-playlist-video-renderer[{n}]/div[2]/div[1]/ytd-thumbnail/a').get_property('href')
        dici = {f'aula{n}':link}
        linkAulas.append(dici)
        n += 1
    except:
        print('erro 404')
        break

os.system('cls')

for numero in range(len(linkAulas)):
    aulasNum = numero + 1
    print(f'Link Tas Aulas {aulasNum} : {linkAulas[numero][f'aula{aulasNum}']}')