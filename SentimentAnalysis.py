import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import codecs

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''

    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = '5DMWfdMhHpl0iePXMTIZb0f6P'
        consumer_secret = 'mIBuvqn9FYQamuLYUqj4kxScK8oMHfmCiWzcLP3bNFkPn1djlt'
        access_token = '1000362000885534724-e5IImCXE2dt0vvuoN00N6VaHfq5WMp'
        access_token_secret = 'BhV3PHQsAmHdRf89lAgPVrywsr2ZYobIeagtO5kFOtweT'

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
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        # return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
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
            print("Error: " + str(e))


def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query='Nomura Holdings', count=200)
    num = 2

    if tweets == None:
        print("Couldn't get tweets")
        return

    # Open output file
    out = codecs.open("lib/Output.csv", 'w', encoding="utf-8")

    # Stop execution if output file not found
    if out.closed :
        print("Couldn't open file")
        return

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    out.write("Positive sentiment,{}%,[".format(100 * len(ptweets) / len(tweets)))

    for tweet in ptweets[:10]:
        print(tweet['text'])

    i = 0

    for tweet in ptweets[:num]:

        t = tweet['text']
        out.write(str(t))

        if i != num-1:

            out.write(";")

        i = i + 1

    out.write("]")
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']

    out.write("\n")

    # percentage of negative tweets
    out.write("Negative sentiment,{}%,[".format(100 * len(ntweets) / len(tweets)))

    i = 0

    for tweet in ntweets[:num]:

        t = tweet['text']
        out.write(str(t))

        if i != num-1:

            out.write(";")

        i = i + 1

    out.write("]")

    out.write("\n")

    # percentage of neutral
    out.write("Neutral sentiment,{}%,[]".format(100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets)))

    out.close()


if __name__ == "__main__":
    # calling main function
    main()
