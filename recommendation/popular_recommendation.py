import pandas as pd

class PopularRecommendation:
    """ Popular Recommednation system model """

    def __init__(self):
        """Create an instance of Popular Recommendation"""

    def popular_recommend(self, tags, data):
        """ Given tags return popular artists
          args:
            tags(string): tag for genre of artist

          returns:
            popular_artist(list): list of all the popular artists for given tag

        """
        # load in csv
        popular = pd.read_csv(data)

        # format tags to be filterable
        tags_joined = '|'.join(tags)

        # filter out to only the selected tags
        tags_filtered = popular[popular['tags'].str.contains(
        tags_joined, case=False)]

        # filtered to top 5 highest playcount
        top_5 = tags_filtered.nlargest(5, 'playcount')

        # append the list to our popular list
        top5_list = top_5['name'].to_list()

        # create our popular recommednation list
        popular_artist = top_5['name'].to_list()

        return popular_artist
