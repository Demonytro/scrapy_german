import json
import re

import requests
from bs4 import BeautifulSoup

main_url = "https://www.kleinanzeigen.de"
base_url = "https://www.kleinanzeigen.de/s-haus-garten/c80"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}


def get_urls():
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    pag_content = soup.select('div[class=pagination] a[class="pagination-page"] ')
    pag_urls = [base_url]

    for a in pag_content[:1]:
        pag_url = main_url + a['href']
        pag_urls.append(pag_url)

    urls = []

    for content_url in pag_urls:
        response = requests.get(content_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.select('div[class="aditem-main--middle"] h2[class="text-module-begin"] a')
        for a in content[:1]:
            url = main_url + a['href']
            urls.append(url)

    return urls


def spider(urls):
    data = []
    for url in urls:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.select('article[id="viewad-product"]')

        for el in content:
            result = {}
            title_art = el.find('h1', attrs={"id": "viewad-title"}).text.lstrip()
            price_art = el.find('h2', attrs={"id": "viewad-price"}).text.lstrip()
            location_art = el.find('span', attrs={"id": "viewad-locality"}).text.lstrip()
            data_art = el.find('div', attrs={"id": "viewad-extra-info"}).find('span').text
            # Beschreibung -
            description = el.find('p', attrs={"id": "viewad-description-text"}).text.lstrip()

            result.update({'url': url,
                           'title': title_art,
                           'price': price_art,
                           'location': location_art,
                           'data': data_art,
                           'descritpion': description}
                          )

            data.append(result)
    # print(data)
    return data


if __name__ == '__main__':

    url_for_scraping = get_urls()
    # print(url_for_scraping)
    r = spider(url_for_scraping)
    with open('enemy.json', 'w', encoding='utf-8') as fd:
        json.dump(r, fd, ensure_ascii=False)

