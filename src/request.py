from aiohttp_requests import requests

WIKI_HOST = 'https://feheroes.gamepedia.com'


async def requestApiQuery(queryParams):
    defaultQueryParams = {
        'action': 'query',
        'format': 'json',
    }

    allQueryParams = {**defaultQueryParams, **queryParams}

    # fetch and parse as json
    response = await requests.get(f'{WIKI_HOST}/api.php', params=allQueryParams)
    payload = await response.json()

    # extract meaningful data from API response
    cargoquery = payload.get('cargoquery', [])
    return [row.get('title') for row in cargoquery]
