#  python library imports
import string
import re
import nltk
import en_core_web_sm
from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords


nlp = en_core_web_sm.load()

TKNZ = TweetTokenizer()
LEM = WordNetLemmatizer()
STOP_WORDS = stopwords.words('english') 



def filter_tweets(tweets_list, expr):
    output = []

    try: # list of tweets
        for tweet in tweets_list:
            text = tweet['text']
            found =  re.search(expr, text)
            if found:
                output.append(tweet['text'])

    except: # list of tweet 'text' body
        for text in tweets_list:
            found =  re.search(expr, text)
            if found:
                output.append(text)

    return output

def filter_tweets_with_list(tweets_list, phrases):
    output = []
    for tweet in tweets_list:
        tokens = tokenize_tweet(tweet)
        if any(word in phrases for word in tokens):
            output.append(tweet)
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

def get_names(text):
    global nlp
    article = nlp(text)
    labels = [x.label_ for x in article.ents]
    [(x.orth_,x.pos_, x.lemma_) for x in [y 
                                      for y
                                      in nlp(text) 
                                      if not y.is_stop and y.pos_ != 'PUNCT']]
    parts_of_speech = dict([(str(x), x.label_) for x in nlp(text).ents])
    names = []
    # print(text)
    # print('\n')
    # print("parts of speech:", parts_of_speech)
    # print('\n')
    # print('-----------------------------')
    for (key, value) in parts_of_speech.items() :
        if(value == "PERSON") :
            names.append(key)
    return names 

def get_parts_of_speech(text):
    global nlp
    article = nlp(text)
    labels = [x.label_ for x in article.ents]
    [(x.orth_,x.pos_, x.lemma_) for x in [y 
                                      for y
                                      in nlp(text) 
                                      if not y.is_stop and y.pos_ != 'PUNCT']]
    parts_of_speech = dict([(str(x), x.label_) for x in nlp(text).ents])
    return parts_of_speech

def remove_stopwords_from_award(award):
    award_stop_words = ["by", "a", "an", "for", "in", "or", "-"]

    award_keywords = []
    for word in award.split():
        if word not in award_stop_words:
            award_keywords.append(word)
    return award_keywords

def filter_award_tweets(data, award):
    try:
        tweets_with_award = []
        # non important award words
        award_stop_words = ["by", "a", "an", "for", "in", "or", "-"]
        # important words for this award 
        award_keywords = []
        for word in award.split():
            if word not in award_stop_words:
                award_keywords.append(word)
    #     print(award_keywords)
        for tweet in data: 
            tweet_text = tweet['text']
            # text of each tweet 
            if all(keyword in tweet_text.lower() for keyword in award_keywords):
                tweets_with_award.append(tweet_text)
        return tweets_with_award
    
    except:
        tweets_with_award = []
        # non important award words
        award_stop_words = ["by", "a", "an", "for", "in", "or", "-"]
        # important words for this award 
        award_keywords = []
        for word in award.split():
            if word not in award_stop_words:
                award_keywords.append(word)
    #     print(award_keywords)
        for tweet in data: 
            # text of each tweet 
            if all(keyword in tweet.lower() for keyword in award_keywords):
                tweets_with_award.append(tweet)
        return tweets_with_award

def filter_tweets_remove(tweets, param):
    matches =[]
    for tweet in tweets:
        found = re.search(param, tweet, flags=re.IGNORECASE)
        if(not found):
                 matches.append(tweet)

    return matches

