#  python library imports
import en_core_web_sm
import tokenize
import operator

# local file imports
from util import *

nlp = en_core_web_sm.load()

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
    

def get_type_of_name(text, item_type):
    """
    Gets NER from sentence using NLTK
    """
    article = nlp(text)
    labels = [x.label_ for x in article.ents]
    [(x.orth_,x.pos_, x.lemma_) for x in [y 
                                      for y
                                      in nlp(text) 
                                      if not y.is_stop and y.pos_ != 'PUNCT']]
    parts_of_speech = dict([(str(x), x.label_) for x in nlp(text).ents])
    names = []
    for (key, value) in parts_of_speech.items() :
        # entity_type for people: 'PERSON'
        # entity_type for movie: 'WORK_OF_ART'
        if(value == item_type) :
            names.append(key)
#     print(names)
    return names 

def _get_winner(data, awards):
    # Your code here
    # declare dictionary for winners (award: winner)
    winners = {key: "" for key in awards} 
    
    for award in awards:
    # Get tweets with keyword award 
        tweets_with_award = filter_award_tweets(data, award)
        
        winner_name_count = {}
        for tweet in tweets_with_award: 
            # movies are categorized as WORK_OF_ART
            entity_type = "WORK_OF_ART"
            # awards with these keywords represent people winning 
            if "actor" in award.lower() or "actress" in award.lower() or "cecil" in award.lower():
                entity_type = "PERSON"

            names = get_type_of_name(tweet, entity_type)
            for name in names :
                if name.lower() in ["#goldenglobes", "rt @goldenglobes", "cecil b. demille", "goldenglobes", "goldenglobe", "golden", "globes", "golden globes", "golden globe"]:
                    continue
                if name in winner_name_count :
                    winner_name_count[name] = winner_name_count[name] + 1
                else:
                    winner_name_count[name] = 1

        try:
            winner = max(winner_name_count.items(), key=operator.itemgetter(1))[0]
        except: 
            winner = ""
        
        #clean winner
        try:
            index = winner.index('\\')
            winner = winner[:index]
        except:
            do = 'nothing'
        try:
            index = winner.index('-')
            winner = winner[:index]
        except:
            do = 'nothing'

        winner.replace('"','')

        winner = clean_tweet(winner)

        # end = len(winner) - 1
        # while winner[end] == ' ':
        #     winner = winner[:end]
        #     end = end - 1

        winners[award] = winner
    return winners 