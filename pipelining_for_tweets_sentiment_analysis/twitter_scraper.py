import tweepy
import pandas as pd
from credentials import credentials as c


# authentication
auth = tweepy.OAuthHandler(c['consumer_key'], c['consumer_secret'])
auth.set_access_token(c['access_token'],c['access_token_secret'])

# creating the api for use

api = tweepy.API(auth)

# writing a method to get tweets by a search key
search_key = "endsars"

# this returns 50 tweets bundled into a iterator object
tweets = tweepy.Cursor(api.search, q=search_key,lang="en").items(10)

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

# returning the tweets attributes
tweet_created_at_list = []
tweet_id_list = []
tweet_text_list = []
tweet_source_list = []
tweet_coordinate_list = []
tweet_retweet_count_list = []
tweet_likes_count_list = []
user_id_list = []
user_name_list = []
user_screen_name_list = []
user_location_list = []
user_followers_count_list = []
user_friends_count_list = []
user_created_at_list = []
user_is_verified_list = []
user_description_list = []


for tweet in tweets_list:
    tweet_created_at_list.append(tweet.created_at)
    tweet_id_list.append(tweet.id_str)
    tweet_text_list.append(tweet.text)
    tweet_source_list.append(tweet.source)
    tweet_coordinate_list.append(tweet.coordinates)
    tweet_retweet_count_list.append(tweet.retweet_count)
    tweet_likes_count_list.append(tweet.favorite_count)
    user_id_list.append(tweet.user.id_str)
    user_name_list.append(tweet.user.name)
    user_screen_name_list.append(tweet.user.screen_name)
    user_location_list.append(tweet.user.location)
    user_followers_count_list.append(tweet.user.followers_count)
    user_friends_count_list.append(tweet.user.friends_count)
    user_created_at_list.append(tweet.user.created_at)
    user_is_verified_list.append(tweet.user.verified)
    user_description_list.append(tweet.user.description)

tweets_df = pd.DataFrame( {
    "tweet_created_at": tweet_created_at_list,
    "tweet_id" : tweet_id_list,
    "tweet_text" : tweet_text_list,
    "tweet_source" : tweet_source_list,
    "tweet_coordinate" : tweet_coordinate_list,
    "tweet_retweet_count" : tweet_retweet_count_list,
    "tweet_likes_count" : tweet_likes_count_list,
    "user_id_list" : user_id_list,
    "user_name_list": user_name_list,
    "user_screen_name_list": user_screen_name_list,
    "user_location_list": user_location_list,
    "user_followers_count_list": user_followers_count_list,
    "user_friends_count_list": user_friends_count_list,
    "user_created_at_list": user_created_at_list,
    "user_is_verified_list": user_is_verified_list,
    "user_description_list": user_description_list
})

print(tweets_df.head(10))