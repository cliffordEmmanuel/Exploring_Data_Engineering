import tweepy
import pandas as pd
import time
from credentials import credentials as c


# authentication
auth = tweepy.OAuthHandler(c['consumer_key'], c['consumer_secret'])
auth.set_access_token(c['access_token'],c['access_token_secret'])

# creating the api for use

api = tweepy.API(auth)

# writing a method to get tweets by a search key
search_key = "endsars -filter:retweets"  # to filter retweets...

# working with the standard api rate limitations
# you can make ~ 900 api calls every 15 minutes.
# creating a scrape tweets function

def scrapeTweets(search_key, number_of_tweets, number_of_calls):
    """"downloads a specified number of tweets based on the search key by making a specified number of calls to the standard twitter api endpoint."""
    
    print("Creating a dataframe to store tweets....")
    tweets_df = pd.DataFrame([])


    for call in range(number_of_calls):
        # this returns tweets bundled into a iterator object
        print(f"Making API call number: {call+1}...")
        tweets = tweepy.Cursor(api.search, q=search_key,lang="en").items(number_of_tweets)
        tweets_list = [tweet for tweet in tweets]

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


        single_run_df = pd.DataFrame( {
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

        tweets_df = pd.concat([tweets_df,single_run_df])

        print("Waiting for 2 mins to make the next call...")
        time.sleep(120) # wait for ~ 15min before the next api call

    return tweets_df




result = scrapeTweets(search_key,10,6)

result.to_csv("test.csv")
print("data saved!!...")