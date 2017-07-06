from bs4 import BeautifulSoup
import requests

from util import save_data_to_file, extract_data

url = "http://www.dialadeliverykenya.co.ke/chicken-inn-menu"
json_file = "chicken_inn.json"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

items = soup.find_all('div', class_='tab-inner chicken-padder')

structured_items = [extract_data(item, url) for item in items]

save_data_to_file(structured_items, json_file)

