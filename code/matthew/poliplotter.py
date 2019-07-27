# filename: poliplotter.py

import re # used to clean tweets
import tweepy # used in API authorization
from textblob import TextBlob # used to parse individual words
import matplotlib.pyplot as plt # used to help plot word cloud
from wordcloud import WordCloud, STOPWORDS # used to generate word cloud and remove stopwords

# ***** AUTHENTICATION *****
# ***** HIDDEN FROM GITHUB *****

try:
    # Creates the authentication object
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # Sets access token and secret
    auth.set_access_token(access_token, access_token_secret)
    # creates tweepy API object to fetch tweets
    api = tweepy.API(auth)
except:
    print("\nError: Authentication Failed\n")
    quit()


name = input("\nWithout including the @ symbol,\nPlease type the username of the requested account: ") # specifies target user
tweetCount = int(input("How many tweets would you like to analyze? ")) # number of tweets to pull

# calls the user_timeline function with our parameters
results = api.user_timeline(id=name, count=tweetCount, tweet_mode="extended")

# cycles through full results, checks against RTs and then adds the rest to one complete string
tweet_string = ""
for tweet in results:
    full_tweet = tweet.full_text
    if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
        tweet_string += full_tweet

def clean_tweet(tweets):
    """Uses regex statements to clean tweets by removing links and special characters"""
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweets).split())


clean_tweets = clean_tweet(tweet_string) # cleans tweets
tweet_words = TextBlob(clean_tweets)
words = tweet_words.words # separates into individual words
word_string = " ".join(words) # joins as one string

# establishes stopwords
stopwords = set(STOPWORDS)
stopwords.update(["amp", "will", "need"])

# creates the wordcloud object
wordcloud = WordCloud(width=480, height=480, background_color="white", stopwords=stopwords, margin=0).generate(word_string)

# displays the generated image
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
