import json
import os
import re
from os.path import join, normpath


class ApiObject(object):

    def to_string(self):
        string = ""

        for item in self.__dict__.items():
            string += "{} = {},\n".format(item[0], item[1])

        return string


def extract_data(item, url):
    result = ApiObject()

    result.image_url = normpath(join(url, item.find('img')['src']))
    title_item = item.find('h3')
    result.title = title_item.get_text()
    result.title_extra = ""

    if title_item.find_next().name == 'h4':
        result.title_extra = item.find('h4').get_text()

    selections = []

    table = item.find('table')
    td = table.find_all('td')

    for data in td:
        titles = filter(
            lambda x: bool(x.get_text().strip()),
            data.find_all('h5'))

        for title in titles:
            title_text = title.get_text()
            title_text_extra = ""

            next_element = title.find_next()

            if next_element.name == 'h4':
                title_text_extra = next_element.get_text()

                amount = next_element.find_next().get_text()
            else:
                amount = next_element.get_text()

            selections.append({
                'title': title_text,
                'title_extra': title_text_extra,
                'amount': amount,
            })

        other_titles = [re.sub(r'\n', '', item.get_text()) for item in data.select('p strong')]

        for i in range(len(other_titles)):
            if i % 2 == 0:
                selections.append({
                    'title': other_titles[i],
                    'title_extra': '',
                    'amount': other_titles[i+1],
                })

    result.selections = tuple(selections)

    return result


def extract_json_data(items):
    return json.dumps(items, default=lambda x: x.__dict__, sort_keys=True, indent=4)


def save_data_to_file(items, file_name):
    json_data = extract_json_data(items)

    json_file = join(os.path.dirname(os.path.abspath(__file__)), "data/" + file_name)

    with open(json_file, 'w') as f:
        f.write(json_data)

        print('Saved data to the file: ', json_file)
