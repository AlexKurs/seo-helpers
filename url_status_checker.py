import requests
from bs4 import BeautifulSoup
import csv


# Wordpress SEO Yast Sitemaps Checker


def checker():
    website = 'https://'
    sitemap = website + '/sitemap_index.xml'

# Kategorie parsen

    r = requests.get(sitemap)
    doc = BeautifulSoup(r.text, 'html.parser')
    links = doc.find_all('loc')
    date = []

    for i in links:
        url = i.text
        date.append(url)

# URLs aus Kategorien parsen

    liste = []

    for link in date:
        source = link
        response = requests.get(source)
        doc = BeautifulSoup(response.text, 'html.parser')
        urls = doc.find_all('loc')
        for x in urls:
            url = x.text
            liste.append(url)

# Status Code Checker

    for url in liste:
        r = requests.get(url)
        status = r.status_code
        print(status, url)
    return liste


checker()
print('Fertig')
