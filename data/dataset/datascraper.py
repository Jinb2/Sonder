from utils import lastfm_get, jprint
from IPython.core.display import clear_output
import pandas as pd
import time
import requests_cache

requests_cache.install_cache()

def scraper():
    #TODO change parameters to ask for what data info you want
    """Sends requests to lastfm and appends to list"""

    # stores our responses
    responses = []

    page = 1
    total_pages = 99999 # dummy number

    #loop for requesting data
    while page <= total_pages:

        payload = {
            'method': 'chart.gettopartists',
            'limit': 500,
            'page': page
        }

        print("Requesting page {}/{}".format(page, total_pages))

        #clear the output
        clear_output(wait = True)

        #send our requests
        response = lastfm_get(payload)

        # if our request is invalid
        if response.status_code != 200:
            print(response.text)
            break

        #extract pagination info
        page = int(response.json()['artists']['@attr']['page'])
        total_pages = int(response.json()['artists']['@attr']['totalPages'])

        #append to list
        responses.append(response)

         # if it's not a cached result, sleep
        if not getattr(response, 'from_cache', False):
            time.sleep(0.25)

        # increment the page number
        page += 1

    return responses
