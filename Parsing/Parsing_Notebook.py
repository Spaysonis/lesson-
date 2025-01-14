import base64


import requests
from bs4 import BeautifulSoup

#  Напишите скрапер, который получит список всех ноутбуков с сайта включая их детальную информацию.
#  Для работы используем библиотеки bs4, requests.

url = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops'
response = requests.get(url)
page = 1
if response.status_code == 200:
    print('Соединение установленно!! ')
    page_content = response.text
    soup = BeautifulSoup(page_content, 'html.parser')

    laptops = soup.find_all('div', class_='col-md-4 col-xl-4 col-lg-4')
    #print(laptops)

    for laptop in laptops:
        name = laptop.find('a', class_='title').text.strip()
        price = laptop.find('h4', class_='price float-end card-title pull-right').text.strip()

        
        print(name, price)
else:
    print(response.status_code)