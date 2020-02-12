import spacy
import operator
nlp = spacy.load("en_core_web_sm")


def filter_presenter_tweets(data, award):
    tweets_with_presenters = []
    # non important award words        
    award_stop_words = ["best", "by", "a", "an", "for", "in", "or", "-"]
    # important words for this award 
    award_keywords = []
    for word in award.split():
        if word not in award_stop_words:
            award_keywords.append(word)
#     print(award_keywords)
    present_words = ["present", "presented", "presents", "presentor", "presentors"]
    for tweet in data: 
        tweet_text = tweet
        if any(pres_keyword in tweet_text.lower() for pres_keyword in present_words) and any(a in tweet_text.lower() for a in award_keywords):
            # print(tweet_text)
            tweets_with_presenters.append(tweet_text)
    return tweets_with_presenters

def get_name_with_type(text, entity_type):
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
            # print(key, value)
            if(value == entity_type) :
                names.append(key)
        return names 

def _get_presenters(data, awards):
    '''Hosts is a list of one or more strings. Do NOT change the name
    of this function or what it returns.'''
    # declare dictionary for winners (award: winner)
    # presenters = {key: "" for key in awards} 
    presenters = {}
    for award in awards:
    # Get tweets with keyword award 
        tweets_with_award = filter_presenter_tweets(data, award)
        presenter_name_count = {}
        for tweet in tweets_with_award: 
            # movies are categorized as WORK_OF_ART
            entity_type = "PERSON"
            names = get_name_with_type(tweet, entity_type)
            for name in names :
                if name.lower() in ["#goldenglobes", "rt @goldenglobes", "cecil b. demille", "goldenglobes", "goldenglobe", "golden", "globes", "golden globes", "golden globe"]:
                    continue
                if name in presenter_name_count :
                    presenter_name_count[name] = presenter_name_count[name] + 1
                else:
                    presenter_name_count[name] = 1
        two_presenters = [] 
        for i in range(2): 
            top_presenter = max(presenter_name_count.items(), key=operator.itemgetter(1))[0]
            two_presenters.append(top_presenter)
            del presenter_name_count[top_presenter]
        presenters[award] = two_presenters
    return presenters 