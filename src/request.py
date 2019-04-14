from aiohttp_requests import requests
import aiohttp.web
import logging

from src.constants import API_BATCH_SIZE, WIKI_HOST


async def requestApiQuery(queryParams):
    defaultQueryParams = {"action": "query", "format": "json", "formatversion": 2}
    allQueryParams = {**defaultQueryParams, **queryParams}

    logging.info(f"requestApiQuery: {allQueryParams}")

    # fetch and parse as json
    response = await requests.get(f"{WIKI_HOST}/api.php", params=allQueryParams)
    payload = await response.json()

    # extract meaningful data from API response
    cargoquery = payload.get("cargoquery", [])
    rows = [row.get("title") for row in cargoquery]
    logging.debug(f"requestApiQuery.response: {rows}")

    return rows


async def requestApiRows(queryParams, offset=0):
    rows = await requestApiQuery({**queryParams, "offset": offset, "limit": API_BATCH_SIZE})

    if len(rows) < API_BATCH_SIZE:
        return rows

    nextRows = await requestApiRows(queryParams, offset + API_BATCH_SIZE)
    return rows + nextRows
