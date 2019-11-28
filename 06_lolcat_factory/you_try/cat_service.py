import os
import shutil

import requests


def get_cat(folder, cat_name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data_from_url(url)
    save_data(folder, cat_name, data)


def save_data(folder, cat_name, data):
    file_path = os.path.join(folder, cat_name + ".jpg")
    with open(file_path, 'wb') as fout:
        shutil.copyfileobj(data, fout)


def get_data_from_url(url):
    response = requests.get(url, stream=True)
    return response.raw
