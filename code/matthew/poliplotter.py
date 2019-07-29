# filename: poliplotter.py

import re # used to clean tweets
import tweepy # used in API authorization
import numpy as np # used for reading the mask images
from PIL import Image # also used for reading the mask images
from textblob import TextBlob # used to parse individual words
import matplotlib.pyplot as plt # used to help plot word cloud
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator # used to generate word cloud and remove stopwords

# ***** AUTHENTICATION *****
# ***** HIDDEN FOR SECURITY *****

def authenicator():
    """creates the authenication object, sets access token and secret, then creates the tweepy API object to fetch tweets"""
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
    except:
        print("\nError: Authentication Failed\n")
        quit()
    return api

def target_user():
    name = input("\nWithout including the @ symbol,\nPlease type the username of the requested account: ") # specifies target user
    tweetCount = int(input("How many tweets would you like to analyze? ")) # number of tweets to pull
    mask = np.array(Image.open("img/trump_portrait.jpg")) # opens the image file, converts to a NumPy array and stores as the "mask" variable
    return name, tweetCount, mask

def results(api, name, tweetCount):
    """gathers x number of tweets from the user and returns the results"""
    results = api.user_timeline(id=name, count=tweetCount, tweet_mode="extended")
    return results

def compiler(results):
    """cycles through full results, checks against RTs and then adds the rest to one complete string"""
    tweet_string = ""
    for tweet in results:
        full_tweet = tweet.full_text
        if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
            tweet_string += full_tweet
    return tweet_string

def clean_tweet(tweets):
    """Uses regex statements to clean tweets by removing links and special characters"""
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweets).split())

def string_prep(clean_tweets):
    """prepares the tweets for later use by the wordcloud function"""
    tweet_words = TextBlob(clean_tweets) # allows for tweets to be manipulated
    words = tweet_words.words # creates a WordList
    word_string = " ".join(words) # joins as one string
    return word_string

def stopwords():
    """establishes stopwords and adds on some custom ones"""
    stopwords = set(STOPWORDS)
    stopwords.update(["amp", "will", "need", "much", "us", "Im", "cant", "going", "thats"])
    return stopwords

def wordcloud(word_string, stopwords):
    """creates the wordcloud object"""
    try:
        wc = WordCloud(stopwords=stopwords, background_color="white", max_words=10000, mask=mask).generate(word_string)
        return wc
    except ValueError:
        print(f"We're sorry. '{name}' is not a valid Twitter user.\n")
        quit()

def show(mask, wc):
    """displays the generated image"""
    image_colors = ImageColorGenerator(mask) # create color from image
    plt.figure(figsize=[16,9])
    plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    plt.show()

if __name__ == '__main__':
    api = authenicator()
    name, tweetCount, mask = target_user()
    results = results(api, name, tweetCount)
    tweet_string = compiler(results)
    clean_tweets = clean_tweet(tweet_string)
    word_string = string_prep(clean_tweets)
    stopwords = stopwords()
    wc = wordcloud(word_string, stopwords)
    show(mask, wc)
