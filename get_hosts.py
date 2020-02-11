#  python library imports
import tokenize
import operator

# local file imports
from util import *


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
    
    return [winner1]
    

