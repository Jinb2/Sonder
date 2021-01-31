from datascraper import scraper
from tqdm import tqdm


# create our dataframe
# TODO create into a class
responses = scraper()
r0 = response[0]
r0_json = r0.json()
r0_artists = r0_json['artists']['artist']
r0_df = pd.DataFrame(r0_artists)
r0_df.head()

# list comprehension (combine into one dataframe)
frames = [pd.DataFrame(r.json()['artists']['artist']) for r in responses]
artists = pd.concat(frames)
artists.head()

#remove images
artists = artists.drop('image', axis=1)
artists.head()

tqdm.pandas()

# adds tags into our dataframe
artists['tags'] = artists['name'].progress_apply(lookup_tags)

# convert columns into numeric
artists[["playcount", "listeners"]] = artists[["playcount", "listeners"]].astype(int)

# sort the list
artists = artists.sort_values("listeners", ascending=False)
artists.head(10)

#drop any nan values
artist = artist.dropna(how='all')  

# export into csv
artists.to_csv('artists.csv', index=False)
