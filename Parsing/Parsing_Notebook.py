import pprint
import requests
from bs4 import BeautifulSoup



start_url = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops'



def parser_note_book(b_url):

    laptop_data = []
    current_page = 1

    while True:
        url = f'{b_url}?page={current_page}'
        try:
            response = requests.get(url)
            response.raise_for_status()  # query status check == 200 is OK
        except requests.exceptions.RequestException as e:
            print(f'Error connect!! Status = {e}')
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        laptops = soup.find_all('div', class_='col-md-4 col-xl-4 col-lg-4')

        if not laptops:
            print('Ноутбуки не найдены или страниц больше нет.')
            break

        print(f'Parsing page {current_page}')
        for laptop in laptops:
            try:
                name_book = laptop.find('p', class_='description card-text').text.split(',')[0]
                price_book = laptop.find('h4', class_='price float-end card-title pull-right').text.strip()
                parameter_book = laptop.find('p', class_='description card-text').text.strip()
                laptop_data.append({'model':name_book, 'price':price_book,'parameter':parameter_book})
            except AttributeError:
                print('Ошибка в структуре данных для одного из ноутбуков.')
                continue

        next_page = soup.find('a', rel='next')

        if next_page:
            current_page += 1
        else:
            print('-->!END!<--')
            break
    print(f'Пройдено {current_page} страниц!')
    display_data(laptop_data)


def display_data(laptop_data):

    for i in laptop_data:
        pprint.pprint(i)
        print()


parser_note_book(start_url)



