import requests
from bs4 import BeautifulSoup



base_url = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops'
currency_page = 1

while True:
    url = f'{base_url}?page={currency_page}'
    response  = requests.get(url)

    if response.status_code != 200:
        print('ошибка соединения!')
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    laptops = soup.find_all('div', class_='col-md-4 col-xl-4 col-lg-4')

    if not laptops:
        print('Ноутбуки не найдены! ')
        break

    print(f'Страница {currency_page}')
    for laptop in laptops:
        name_book = laptop.find('a', class_='title').text.strip()
        price_book = laptop.find('h4', class_='price float-end card-title pull-right').text.strip()

        print(f'Model: {name_book}| Price: {price_book}')

    next_page = soup.find('a', rel='next')

    if next_page:
        currency_page += 1
    else:
        print(f'---->>ПАРСИНГ ЗАВЕРШЕН!<<----')
        print(f'ВСЕГО {currency_page} СТРАНИЦ!')
        break
