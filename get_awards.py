# from imdb import IMDb
# from imdb.Person import Person
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import string
import re
import operator
from util import *


def _get_awards(data):
    award_words = ['actor', 'actress', 'animated', 'best', 'comedy', 'director', 'drama', 'feature', 'film', 'foreign', 'language', 'mini', 'mini-series', 'motion', 'musical', 'orginal', 'original', 'performance', 'picture', 'role', 'score', 'screenplay', 'series', 'song', 'supporting', 'television']
    helper_words = ['by','an','in', 'a','for','-','or']

    award_count = {}
    awards = []
    award_tweets = []
    for tweet in data:
        tweet = tweet.lower()
        tweet = tokenize_tweet(tweet)
        if len(set(award_words).intersection(set(tweet))) > 3:
            award_tweets.append(tweet)

    for tweet in award_tweets:
        potential_award = []
        start = False
        encountereted_hyphen = False
        for word in tweet:
            if start == True:
                if word == '-' and encountereted_hyphen == False:
                    potential_award.append(word)
                    encountereted_hyphen = True
                elif word == '-' and encountereted_hyphen == True:
                    continue
                elif word in award_words or word in helper_words:
                    potential_award.append(word)
            elif word == 'best':
                potential_award.append(word)
                start = True
            else:
                break
        if start:
            try:
                hyphen_index = potential_award.index('-')
                if hyphen_index != -1:
                    potential_award = potential_award[:hyphen_index] + potential_award[hyphen_index+1:].remove('-')
            except:
                do = 'nothing'

            # GET SET OF KEY WORDS FOR POTENTIAL AWARD
            # non important award words 
            award_stop_words = ["by", "a", "an", "for", "in", "or", "-"]
            potential_award_keywords = []
            for word in potential_award:
                if word not in award_stop_words:
                    potential_award_keywords.append(word)

            potential_award_keywords.sort()

            potential_award = ' '.join(potential_award)

            cur_keys = list(award_count.keys())

            award_keywords_list = []

            keyword_dic = {}

            # GET SET OF ALL KEYWORDS FOR ALL KEYS
            for key in cur_keys:
                # important words for this award 
                award_keywords = []
                for word in key.split():
                    if word not in award_stop_words:
                        award_keywords.append(word)
                award_keywords.sort()
                keyword_dic[freeze_set(award_keywords)] = key
                award_keywords_list.append(freeze_set(award_keywords))
             
            if potential_award_keywords in award_keywords_list:
                true_award = keyword_dic[freeze_set(potential_award_keywords)] 
                award_count[true_award] = award_count[true_award] + 1
            else:
                award_count[potential_award] = 1   
    
    awards = []
    for _ in range(27):
        award = max(award_count.items(), key=operator.itemgetter(1))[0]
        awards.append(award)
        del award_count[award]
    awards.sort()

    return awards

def freeze_set(s):
    return ''.join(s)

# given an award_list, only return awards that are not duplicates of "award"
def filter_duplicate_awards(award_list, award):
    unique_awards = [] 
    # non important award words 
    award_stop_words = ["by", "a", "an", "for", "in", "or", "-"]
    # important words for this award 
    award_keywords = []
    for word in award.split():
        if word not in award_stop_words:
            award_keywords.append(word.lower())
    for a in award_list:
        if all(keyword in a.lower() for keyword in award_keywords):
            unique_awards.append(a)
    return unique_awards
    
