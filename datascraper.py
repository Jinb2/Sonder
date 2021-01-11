import requests
import os

def lastfm_get(payload):
    """Sends request to lastfm.

    args:
        payload: dictionary of keys

    returns:
        response: status of request
    """

    # user-agent header
    USER_AGENT = os.environ.get('USER_AGENT')
    headers = {'user-agent': USER_AGENT}

    # API key
    API_KEY = os.environ.get('API_KEY')

    # add API and format to payload
    payload['api_key'] = API_KEY
    payload['format'] ='json'

    # API root url
    url = 'http://ws.audioscrobbler.com/2.0/'

    # sends request
    response = requests.get(url, headers=headers, params=payload)

    return response


r = lastfm_get({
    'method': 'chart.gettopartists'
})

print(r.status_code)
