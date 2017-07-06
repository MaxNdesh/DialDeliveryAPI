from bs4 import BeautifulSoup
import requests

from util import extract_data, save_data_to_file

url = 'http://www.dialadeliverykenya.co.ke/galitos-menu'
json_file = "galitos_inn.json"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

items = soup.find_all('div', class_='tab-inner galitos-padder')

structured_items = [extract_data(item, url) for item in items]

save_data_to_file(structured_items, json_file)

