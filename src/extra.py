from json import loads
from functools import lru_cache

@lru_cache(maxsize=None)
def get_caches():
    with open("static/data.json", 'r', encoding='utf-8') as file:
        return loads(file.read())

@lru_cache(maxsize=None)
def get_data(data_name):
    data = get_caches()
    return data.get(data_name,"")

@lru_cache(maxsize=None)
def get_multiple_data(data_name):
    result = ""
    data = get_caches()
    data = data.get(data_name,[])
    for dt in data:
        result += dt + "\n"
    return result
    