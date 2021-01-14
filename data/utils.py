import json
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
    payload['format'] = 'json'

    # API root url
    url = 'http://ws.audioscrobbler.com/2.0/'

    # sends request
    response = requests.get(url, headers=headers, params=payload)

    return response


def jprint(obj):
    """Helper function to print json in more readable format"""

    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def lookup_tags(artist):
    """
    args:
        artist: name of artist you are looking up
    returns:
        tags_str: string of most popular tags
    """
    response = lastfm_get({
        'method': 'artist.getTopTags',
        'artist':  artist
    })

    # if there's an error, just return nothing
    if response.status_code != 200:
        return None

    # extract the top three tags and turn them into a string
    tags = [t['name'] for t in response.json()['toptags']['tag'][:3]]
    tags_str = ', '.join(tags)

    # rate limiting
    if not getattr(response, 'from_cache', False):
        time.sleep(0.25)
    return tags_str
