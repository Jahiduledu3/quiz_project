import requests

api_url = 'https://opentdb.com/api.php?amount=20'


def raw_data(input_url):
    response = requests.get(input_url)
    response_json = response.json()['results']
    return response_json


data = raw_data(api_url)
