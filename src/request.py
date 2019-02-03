import requests

WIKI_HOST = 'https://feheroes.gamepedia.com'


def requestApiQuery(queryParams):
    defaultQueryParams = {
        'action': 'query',
        'format': 'json',
    }

    allQueryParams = {**defaultQueryParams, **queryParams}

    # fetch and parse as json
    response = requests.get(f'{WIKI_HOST}/api.php', params=allQueryParams)
    payload = response.json()

    # extract meaningful data from API response
    cargoquery = payload.get('cargoquery', [])
    return [row.get('title') for row in cargoquery]
