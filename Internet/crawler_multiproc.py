import requests
import csv

from bs4 import BeautifulSoup
from datetime import datetime
from multiprocessing import Pool

def get_html(url):
    r = requests.get(url)
    return r.text

def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')

    tds = soup.find('table', id = 'currencies-all').find_all('td', class_='currency-name')
    links = []
    for td in tds:
        a = td.find('a').get('href')
        link = 'https://coinmarketcap.com/' + a
        links.append(link)
    return links

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        name = soup.find('h1', class_='details-panel-item--name').text.strip()
    except:
        name = ''

    try:
        price = soup.find('span', id = 'quote_price').text.strip()
    except:
        price = ''

    data = {'name': name,
            'price': price}
    print(data['name'], data['price'])
    return data

def write_csv(data):
    with open('cointmarketcap.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow((data['name'],
                         data['price']))

def make_all(url):
    html = get_html(url)
    data = get_page_data(html)
    write_csv(data)

def main():
    # start = datetime.now()
    url =  'https://coinmarketcap.com/all/views/all/'
    all_links = get_all_links(get_html(url))
    # for index, url in enumerate(all_links):
    #     html = get_html(url)
    #     data = get_page_data(html)
    #     write_csv(data)
    #     print(index)
    with Pool(8) as p:
        p.map(make_all, all_links)
    # end = datetime.now()
    # total = end - start
    # print(str(total))

if __name__ == '__main__':
    main()