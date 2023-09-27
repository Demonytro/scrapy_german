import requests
from bs4 import BeautifulSoup

base_url = "https://www.kleinanzeigen.de/s-haus-garten/c80"
base_url = "https://www.kleinanzeigen.de"
# base_url = "https://index.minfin.com.ua/ua/russian-invading/casualties"


def get_urls():
    response = requests.get(base_url)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup)


if __name__ == '__main__':
    get_urls()


