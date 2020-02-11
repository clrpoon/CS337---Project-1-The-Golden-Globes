#  python library imports
import en_core_web_sm
import tokenize
import operator

# local file imports
from util import *

nlp = en_core_web_sm.load()


def _get_redcarpet(data, year):
        
    #filtering with keyword 'dressed'
    tweets_with_dressed = []   

    for tweet in data: 
        tweet_text = tweet
        if("dressed" in tweet_text.lower()) :
            tweets_with_dressed.append(tweet)
            
               
    #filtering with keywords'worst' and 'best'
    tweets_with_best = []
    tweets_with_worst = []
    controversial_tweets = []


    for tweet in tweets_with_dressed:
        tweet_text = tweet
        if("worst" in tweet_text.lower() and "best" not in tweet_text.lower()) :
            tweets_with_worst.append(tweet)
        elif ("best" in tweet_text.lower() and "worst" not in tweet_text.lower()) :
            tweets_with_best.append(tweet)
       
    
    for tweet in tweets_with_dressed:
        if ("best" in tweet_text.lower()) :
            controversial_tweets.append(tweet)
        elif ("worst" in tweet_text.lower()) :
            controversial_tweets.append(tweet)


    #find highest occuring names
    best_dressed_count = {}
    worst_dressed_count = {}
    most_discussed = {}
    controversial_count = {}

       
    #best dressed
    for tweet in tweets_with_best: 
        names = get_names(tweet)
        for name in names :
            if name.lower() in ["goldenglobes", "goldenglobe", "golden", "globes", "golden globes", "golden globe"]:
                continue
            if name in best_dressed_count :
                best_dressed_count[name] = best_dressed_count[name] + 1
            else:
                best_dressed_count[name] = 1
    max_best_dressed = max(best_dressed_count.items(), key=operator.itemgetter(1))[0]
    best_dressed_count.pop(max_best_dressed, None)
    best_runner_up = max(best_dressed_count.items(), key=operator.itemgetter(1))[0]
    
    
    #worst dressed 
    for tweet in tweets_with_worst: 
        names = get_names(tweet)
        for name in names :
            if name.lower() in ["goldenglobes", "goldenglobe", "golden", "globes", "golden globes", "golden globe", "WORST", "worst"]:
                continue              
            if name in worst_dressed_count :
                worst_dressed_count[name] = worst_dressed_count[name] + 1
            else:
                worst_dressed_count[name] = 1
    max_worst_dressed = max(worst_dressed_count.items(), key=operator.itemgetter(1))[0]
    worst_dressed_count.pop(max_worst_dressed, None)
    worst_runner_up = max(worst_dressed_count.items(), key=operator.itemgetter(1))[0]
 

    #most discussed
    for tweet in tweets_with_dressed: 
        names = get_names(tweet)
        for name in names :
            if name.lower() in ["goldenglobes", "goldenglobe", "golden", "globes", "golden globes", "golden globe"]:
                continue
            if name in most_discussed :
                most_discussed[name] = most_discussed[name] + 1
            else:
                most_discussed[name] = 1
    max_discussed = max(most_discussed.items(), key=operator.itemgetter(1))[0]
    
    
    #most controversial
    for tweet in controversial_tweets:
        names = get_names(tweet)
        for name in names : 
            if name.lower() in ["goldenglobes", "goldenglobe", "golden", "globes", "golden globes", "golden globe"]:
                continue
            if name in controversial_count :
                controversial_count[name] = controversial_count[name] + 1
            else: 
                controversial_count[name] = 1
    max_controversy = max(controversial_count.items(), key=operator.itemgetter(1))[0]
    
    
    
    return max_best_dressed, best_runner_up, max_worst_dressed, worst_runner_up, max_discussed, max_controversy

