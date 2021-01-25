
class PopularRecommendation:
    """ Popular Recommednation system model """

    def popular_recommend(tags):
      """ Given tags return popular artists (only up to 2 tags)
        args:
          tags (string): tag for genres of artist

        returns:
          popular_artist (list): list of all the popular artists

      """
      # check if tags are more than 3
      try:
        if len(tags) <= 2:

          # load in csv
          popular = pd.read_csv("popular.csv")

          # format tags to be filterable
          tags_joined = '|'.join(tags)

          # filter out to only the selected tags
          tags_filtered = popular[popular['tags'].str.contains(tags_joined,case=False)]

          # filtered to top 5 highest playcount
          top_5 = tags_filtered.nlargest(5, 'playcount')

          # append the list to our popular list
          top5_list = top_5['name'].to_list()

         # create our popular recommednation list
          popular_artist = top_5['name'].to_list()

          return popular_artist

      except:
          print("Exceeded the tags")
