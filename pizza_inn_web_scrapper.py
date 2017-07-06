from bs4 import BeautifulSoup
from util import extract_data, save_data_to_file

import requests

url = 'http://www.dialadeliverykenya.co.ke/pizza-inn-menu'
json_file = "pizza_inn.json"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

items = soup.find_all('div', class_='tab-inner pizza-padder')

structured_items = [extract_data(item, url) for item in items]

save_data_to_file(structured_items, json_file)

