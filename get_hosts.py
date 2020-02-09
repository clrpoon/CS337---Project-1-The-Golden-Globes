#  python library imports
import en_core_web_sm
import tokenize
import operator

# local file imports
from util import *

nlp = en_core_web_sm.load()

def _get_hosts(year, data):
    double_host_years = [2013, 2014, 2015, 2019, 2021]

    #preprocess each tweet
    tweets_with_hosts = filter_tweets(data, 'host')
    tweets_with_hosts = preprocess_tweets(tweets_with_hosts)
    tweets_with_hosts = remove_stop_words_from_tweets(tweets_with_hosts, ['http', 'golden', 'gg', '@'])

    #untoken each tweet
    for i in range(len(tweets_with_hosts)):
        tweets_with_hosts[i] = ' '.join(tweets_with_hosts[i])

    #get count for each name
    host_name_count = {}
    for tweet in tweets_with_hosts: 
        names = get_names(tweet)
        for name in names:
            if name in host_name_count:
                host_name_count[name] = host_name_count[name] + 1
            else:
                host_name_count[name] = 1
    
    # determine host(s)
    winner1 = max(host_name_count.items(), key=operator.itemgetter(1))[0]
    if year in double_host_years:
        del host_name_count[winner1]
        winner2 = max(host_name_count.items(), key=operator.itemgetter(1))[0]

        return [winner1, winner2]
    else:
        return [winner1]
    
    winner1_count = host_name_count[winner1]
    
    
    del host_name_count[winner2]
    winner3 = max(host_name_count.items(), key=operator.itemgetter(1))[0]
    winner3_count = host_name_count[winner3]
    del host_name_count[winner3]
    winner4 = max(host_name_count.items(), key=operator.itemgetter(1))[0]
    winner4_count = host_name_count[winner4]

    print(winner1)
    print(winner1_count)
    print(winner2)
    print(winner2_count)
    print(winner3)
    print(winner3_count)
    print(winner4)
    print(winner4_count)

    return []

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
    for (key, value) in parts_of_speech.items() :
        if(value == "PERSON") :
            names.append(key)
    return names 