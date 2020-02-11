import nltk
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import string
import numpy
import re
import copy
from nltk.stem import PorterStemmer
from util import *

tokenizer = TweetTokenizer()
stop_words = list(stopwords.words("english")) + ['performance','golden', 'globes', 'globe', 'goldenglobes', 'best', 'losers', 'loser', 'winners', 'winner', 'actor', 'actress', 'actors', 'actresses', 'yay', 'congrats']

def find_nominees(tweet, set_nom, award):
    # clean and tokenize
    o_text = clean_tweet(tweet)
    text = tokenizer.tokenize(o_text)
    # remove stop words
    clean_text = []
    for t in text:
        if t not in stop_words:
            clean_text.append(t)
    # tag tokenized tweet
    tagged = nltk.pos_tag(clean_text)
    names = []
    portstemmer = PorterStemmer()
    stemmed = []
    for token in [c.lower() for c in clean_text]:
        stemmed.append(portstemmer.stem(token))
    nomin_found = False
    for t in nltk.ne_chunk(tagged):
        if type(t) == nltk.tree.Tree:
            valid = True
            if t.label() == 'PERSON':
                poss = []
                for c in t:
                    if str(c[0]).lower() not in award.lower() and str(c[0]).lower() not in stop_words:
                        poss.append(str(c[0]))
                names.append(' '.join([p for p in poss]))
    set_nom_copy = copy.deepcopy(set_nom)

    # check for duplicates
    for n in names:
        if len(set_nom) > 0:
            for s in set_nom_copy:
                if s in n and s in set_nom:
                    set_nom.remove(s)
                    set_nom.add(n)
                elif n not in s :
                    set_nom.add(n)
        else:
            set_nom.add(n)
    return set_nom

def filter_tweets_by_award(tweet_list, award):
    award_stripped = award
    for word in stop_words:
        award_stripped = award_stripped.replace(" " + word + " ", ' ')
    award_no_punct = re.sub(r'[^\w\s]', '', award_stripped)

    tweets = tweet_list
    for token in tokenizer.tokenize(award_no_punct):
        filtered = []
        for text in tweets:
            found =  re.search(token, text) 
            if(found):
                filtered.append(text)
        if len(filtered) > 0:
            tweets = filtered
    return tweets

def _get_nominees(tweet_list, award_list):
    # remove retweets
    rt_filter = []
    for tweet in tweet_list:
        found = re.search("RT", tweet, flags=re.IGNORECASE)
        if(not found):
            rt_filter.append(tweet)
    tweet_list = rt_filter
    nominees = {}
    for award in award_list:
        award_tweet_list = filter_tweets_by_award(tweet_list, award)
        award_nominees = set()
        for tweet in award_tweet_list:
            nom_set = find_nominees(tweet, award_nominees, award)
        for nom in nom_set:
            award_nominees.add(nom)
        nominees[award] = list(award_nominees)
    return nominees