import tweepy
from credentials import credentials as c


# authentication
auth = tweepy.OAuthHandler(c['consumer_key'], c['consumer_secret'])
auth.set_access_token(c['access_token'],c['access_token_secret'])

# creating the api for use

api = tweepy.API(auth)

# writing a method to get tweets by a search key
search_key = "endsars"

# this returns 50 tweets bundled into a iterator object
tweets = tweepy.Cursor(api.search, q=search_key,lang="en").items(50)

tweets_list = [tweet for tweet in tweets]

# what attributes of the tweets do we want to extract
"""
tweet info
    created_at
    id_str
    text
    source
    coordinates
    retweeted_status
    reply_count
    retweet_count
    favorite_count
user bio
    name
    id_str
    followers_count
    screen_name
    location
    description
    verified
    friends(the accounts the user is following)
    favourites_count(the number of tweets the user has liked)
    statuses_count(the number of tweets including retweets issued by the user)
    created_at(the time the account was created )
"""
