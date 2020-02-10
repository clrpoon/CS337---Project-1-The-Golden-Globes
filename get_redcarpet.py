#  python library imports
import en_core_web_sm
import tokenize
import operator

# local file imports
from util import *

nlp = en_core_web_sm.load()


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
    #print(key, value)
    return names 

def _get_redcarpet(data, year):
        
    #filtering with keyword 'dressed'
    tweets_with_dressed = []   

    for tweet in data: 
        tweet_text = tweet['text']
        if("dressed" in tweet_text.lower()) :
            tweets_with_dressed.append(tweet)
            
               
    #filtering with keywords'worst' and 'best'
    tweets_with_best = []
    tweets_with_worst = [] 
    
    for tweet in tweets_with_dressed:
        tweet_text = tweet['text']
        if("worst" in tweet_text.lower()) :
            tweets_with_worst.append(tweet)
        elif ("best" in tweet_text.lower()) :
            tweets_with_best.append(tweet)
            

    #find highest occuring names
    best_dressed_count = {}
    worst_dressed_count = {}
       
    #best dressed
    for tweet in tweets_with_best: 
        names = get_names(tweet["text"])
        for name in names :
            if name.lower() in ["goldenglobes", "goldenglobe", "golden", "globes", "golden globes", "golden globe"]:
                continue
            if name in best_dressed_count :
                best_dressed_count[name] = best_dressed_count[name] + 1
            else:
                best_dressed_count[name] = 1
    max_best_dressed = max(best_dressed_count.items(), key=operator.itemgetter(1))[0]
    best_dressed_count.pop(max_best_dressed, None)
    second_best_dressed = max(best_dressed_count.items(), key=operator.itemgetter(1))[0]
    best_dressed_count.pop(second_best_dressed, None)
    third_best_dressed = max(best_dressed_count.items(), key=operator.itemgetter(1))[0]


    
    
    #worst dressed 
    for tweet in tweets_with_worst: 
        names = get_names(tweet["text"])
        for name in names :
            if name.lower() in ["goldenglobes", "goldenglobe", "golden", "globes", "golden globes", "golden globe", "WORST", "worst"]:
                continue              
            if name in worst_dressed_count :
                worst_dressed_count[name] = worst_dressed_count[name] + 1
            else:
                worst_dressed_count[name] = 1
    max_worst_dressed = max(worst_dressed_count.items(), key=operator.itemgetter(1))[0]
#    worst_dressed_count.pop(max_worst_dressed, None)
#    second_worst_dressed = max(worst_dressed_count.items(), key=operator.itemgetter(1))[0]
#    worst_dressed_count.pop(second_worst_dressed, None)
#    third_worst_dressed = max(worst_dressed_count.items(), key=operator.itemgetter(1))[0]

      
    return max_best_dressed, second_best_dressed, third_best_dressed, max_worst_dressed


_get_redcarpet(data, 2013)