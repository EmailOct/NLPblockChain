# coding: utf-8

# In[41]:


import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import pandas as pd


# In[42]:


class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''

    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'mTmcbfasJjvCVZidOQS5lvcOW'
        consumer_secret = '2u7A5hK2qzN2TykyNjaK4gCRGx3m6gWqqu84FZbQVCRouvTjKp'
        access_token = '2217923042-qML3Xj5DHk5uPbmXFCoCLXd6JJKdTADvHAQ5C1i'
        access_token_secret = 'pGiZMH0KXuLomtq7oSorFSQmoF4sS1TdI1HP1LcRyJsjP'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters using simple regex statements.
        '''
        # return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))

        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count=10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q=query, count=count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))


def main(searchKeyWord):
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query=searchKeyWord, count=20000)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']

    # sentiment = pd.DataFrame()
    pos_sentiment = str(round(100 * len(ptweets) / len(tweets), 2))

    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    neg_sentiment = str(round(100 * len(ntweets) / len(tweets), 2))
    neu_sentiment = str(round(100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets), 2))
    # print(sentiment)

    # percentage of positive tweets
    print("Positive sentiment percentage: {} %".format(pos_sentiment))
    # picking negative tweets from tweets
    # percentage of negative tweets
    print("Negative sentiment percentage: {} %".format(neg_sentiment))
    # percentage of neutral
    print("Neutral sentiment percentage: {} % ".format(neu_sentiment))

    # printing first 5 positive sentiments
    #print("\n\nPositive sentiments:")
    #for tweet in ptweets:
   #     print(tweet['text'])

    # printing first 5 negative sentiments
    #print("\n\nNegative sentiments:")
   # for tweet in ntweets:
    #    print(tweet['text'])
    var = [neu_sentiment, pos_sentiment, neg_sentiment]
    return var
