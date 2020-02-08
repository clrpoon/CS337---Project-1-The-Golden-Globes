import string
import re

def filter_tweets(tweets_list, expr):
    output = []
    try: # list of tweets
        for tweet in tweets_list:
            text = tweet['text']
            found =  re.search(param, text)
            if found:
                output.append(tweet['text'])

    except: # list of tweet 'text' body
        for text in tweets_list:
            found =  re.search(expr, text)
            if found:
                output.append(expr)

    return output 

def clean_tweet(tweet):
    cleaned_tweet = re.sub(r'#[a-z 0-9]+', '', tweet)
    cleaned_tweet = re.sub(r'[^\w\s]', '', cleaned_tweet)

    return cleaned_tweet
