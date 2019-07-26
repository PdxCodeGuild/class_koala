# filename: poliplotter.py

import re
import tweepy
import matplotlib.pyplot as plt
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS

# ***** AUTHENTICATING *****

# Twitter APIs removed for security

try:
    # Creating the authentication object
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # Setting your access token and secret
    auth.set_access_token(access_token, access_token_secret)
    # create tweepy API object to fetch tweets
    api = tweepy.API(auth)
except:
    print("Error: Authentication Failed")


# The Twitter user who we want to get tweets from
name = "mjhwrites"
# Number of tweets to pull
tweetCount = 20

# Calling the user_timeline function with our parameters
results = api.user_timeline(id=name, count=tweetCount, tweet_mode="extended")

# foreach through all tweets pulled
tweet_string = ""
for tweet in results:
    tweet_string += tweet.full_text
    # printing the text stored inside the tweet object

tweet_sentence = TextBlob(tweet_string)
sentences = tweet_sentence.sentences

def clean_tweet(tweets):
    """Cleans tweet by removing links and special characters using regex statements."""
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweets).split())

clean_tweets = clean_tweet(tweet_string)
tweet_word = TextBlob(clean_tweets)
words = tweet_word.words

word_string = " ".join(words)

stopwords = set(STOPWORDS)
stopwords.update(["amp", "will", "need"])

# Create the wordcloud object
wordcloud = WordCloud(width=480, height=480, background_color="white", stopwords=stopwords, margin=0).generate(word_string)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()




# class SentimentAnalysis(object):
#     """Class for sentiment analysis."""
#     def __init__(self):
#         """Initializes the authorization"""

#
#         # attempt authentication
#         try:
#             # Creating the authentication object
#             self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#             # Setting your access token and secret
#             self.auth.set_access_token(access_token, access_token_secret)
#             # create tweepy API object to fetch tweets
#             self.api = tweepy.API(self.auth)
#         except:
#             print("Error: Authentication Failed")
#
#     def clean_tweet(self, tweet):
#         """Cleans tweet by removing links and special characters using regex statements."""
#         return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
#
#     def get_sentiment(self, tweet):
#         """Utility function to classify sentiment of passed tweet
#         using textblob's sentiment method"""
#         # create TextBlob object of passed tweet text
#         analysis = TextBlob(self.clean_tweet(tweet))
#         # set sentiment
#         if analysis.sentiment.polarity > 0:
#             return 'positive'
#         elif analysis.sentiment.polarity == 0:
#             return 'neutral'
#         else:
#             return 'negative'
#
#     def get_tweets(self, query, count):
#         """Main function to fetch tweets and parse them."""
#         # empty list to store parsed tweets
#         tweets = []
#
#         try:
#             # call twitter api to fetch tweets
#             fetched_tweets = self.api.user_timeline(query, count = count)
#
#             # parsing tweets one by one
#             for tweet in fetched_tweets:
#                 # empty dictionary to store required params of a tweet
#                 parsed_tweet = {}
#
#                 # saving text of tweet
#                 parsed_tweet['text'] = tweet.text
#                 # saving sentiment of tweet
#                 parsed_tweet['sentiment'] = self.get_sentiment(tweet.text)
#
#                 # appending parsed tweet to tweets list
#                 if tweet.retweet_count > 0:
#                     # if tweet has retweets, ensure that it is appended only once
#                     if parsed_tweet not in tweets:
#                         tweets.append(parsed_tweet)
#                 else:
#                     tweets.append(parsed_tweet)
#
#             # return parsed tweets
#             return tweets
#
#         except tweepy.TweepError as e:
#             # print error (if any)
#             print("Error : " + str(e))
#
# def main():
#     # creating object of TwitterClient Class
#     api = SentimentAnalysis()
#     # calling function to get tweets
#     tweets = api.get_tweets(query = 'KamalaHarris', count = 20)
#     # picking positive tweets from tweets
#     ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
#     # percentage of positive tweets
#     print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
#     # picking negative tweets from tweets
#     ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
#     # percentage of negative tweets
#     print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
#     # percentage of neutral tweets
#     # xtweets = len(tweets) - len(ntweets) - len(ptweets)
#     # print("Neutral tweets percentage: {} %".format((10*xtweets) - len(tweets)))
#
#     # printing first 5 positive tweets
#     print("\n\nPositive tweets:")
#     for tweet in ptweets[:10]:
#         print(tweet['text'])
#
#     # printing first 5 negative tweets
#     print("\n\nNegative tweets:")
#     for tweet in ntweets[:10]:
#         print(tweet['text'])
#
# if __name__ == "__main__":
#     # calling main function
#     main()
#
#
#
#
#
#
#





# ***** EXAMPLE 2 - TWEETS FROM A SPECIFIC USER *****
#
# # Creating the API object while passing in auth information
# api = tweepy.API(auth)
#
# # The Twitter user who we want to get tweets from
# name = "JoeBiden"
# # Number of tweets to pull
# tweetCount = 10
#
# # Calling the user_timeline function with our parameters
# results = api.user_timeline(id=name, count=tweetCount)
#
# # foreach through all tweets pulled
# for tweet in results:
#    # printing the text stored inside the tweet object
#    print(tweet.text)


# # ***** EXAMPLE 1 - YOUR TIMELINE *****
#
# # Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
# public_tweets = api.home_timeline()
# # foreach through all tweets pulled
# for tweet in public_tweets:
#    # printing the text stored inside the tweet object
#    print(tweet.text)


# # ***** EXAMPLE 3 - FINDING TWEETS USING A KEYWORD *****
#
# # Creating the API object while passing in auth information
# api = tweepy.API(auth)
#
# # The search term you want to find
# query = "Toptal"
# # Language code (follows ISO 639-1 standards)
# language = "en"
#
# # Calling the user_timeline function with our parameters
# results = api.search(q=query, lang=language)
#
# # foreach through all tweets pulled
# for tweet in results:
#    # printing the text stored inside the tweet object
#    print tweet.user.screen_name,"Tweeted:",tweet.text
