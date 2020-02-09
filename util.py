#  python library imports
import string
import re
import nltk
from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords


TKNZ = TweetTokenizer()
LEM = WordNetLemmatizer()
STOP_WORDS = stopwords.words('english') 

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
                output.append(text)

    return output

def lower_tweet(tweet):
    if type(tweet) != str:
        body = tweet['text'].lower()
        return body
    
    return tweet.lower()

def clean_tweet(tweet):
    '''
    removes hashtages and punctuations
    '''
    cleaned_tweet = re.sub(r'#[a-z 0-9]+', '', tweet)
    cleaned_tweet = re.sub(r'[^\w\s]', '', cleaned_tweet)

    return cleaned_tweet

def clean_tweets(tweets):
    for i in range(len(tweets)):    
        tweets[i] = clean_tweet(tweets[i])
    return tweets

def remove_stop_words_from_tweet(tokenized_tweet, add_words=[]):
    global STOP_WORDS
    return [word for word in tokenized_tweet if (word not in STOP_WORDS) and (word not in add_words)]

def remove_stop_words_from_tweets(tokenized_tweets, add_words=[]):
    for i in range(len(tokenized_tweets)):
        tokenized_tweets[i] = remove_stop_words_from_tweet(tokenized_tweets[i], add_words=add_words)

    return tokenized_tweets

def tokenize_tweet(tweet):
    tokens = TKNZ.tokenize(tweet)
    
    return tokens

def lemmatize_tweet(tweet):
    tokens = tweet
    if type(tweet) == str:
        tokens = tokenize_tweet(tweet)
    
    lem_tokens = []
    for token in tokens:
        lem_tokens.append(LEM.lemmatize(token))
    
    return lem_tokens

def preprocess_tweets(tweets):
    output = []
    for tweet in tweets:
        cleaned_tweet = clean_tweet(tweet)
        # lowered_tweet = lower_tweet(cleaned_tweet)
        tokenized_tweet = tokenize_tweet(cleaned_tweet)
        lemmatized_tweet = lemmatize_tweet(tokenized_tweet)

        output.append(lemmatized_tweet)

    return output


