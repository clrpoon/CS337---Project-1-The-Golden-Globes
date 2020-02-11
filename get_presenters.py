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
    for tweet in gg_data: 
        tweet_text = tweet['text']
        if any(pres_keyword in tweet_text.lower() for pres_keyword in present_words):
#             count = 0 
#             for k in award_keywords:
#                 if k in tweet_text.lower():
#                     count+=1
#             if count/len(award_keywords) >= 0.5:
#             print(tweet_text)
#             print("-------------------------------------------------------------------------------------")
            tweets_with_presenters.append(tweet_text)
    return tweets_with_presenters

def _get_presenters(data, awards):
    '''Hosts is a list of one or more strings. Do NOT change the name
    of this function or what it returns.'''
    # declare dictionary for winners (award: winner)
    presenters = {key: "" for key in awards} 
    
    for award in awards:
    # Get tweets with keyword award 
        tweets_with_award = filter_presenter_tweets(data, award)
#         print(tweets_with_award)
#         tweets_with_award = preprocess_tweets(tweets_with_award)
#         tweets_with_award = remove_stop_words_from_tweets(tweets_with_hosts, ['http', 'golden', 'gg', '@'])
        
        presenter_name_count = {}
        for tweet in tweets_with_award: 
            # movies are categorized as WORK_OF_ART
            entity_type = "PERSON"
            names = get_type_of_name(tweet, entity_type)
            for name in names :
                if name.lower() in ["#goldenglobes", "rt @goldenglobes", "cecil b. demille", "goldenglobes", "goldenglobe", "golden", "globes", "golden globes", "golden globe"]:
                    continue
                if name in presenter_name_count :
                    presenter_name_count[name] = presenter_name_count[name] + 1
                else:
                    presenter_name_count[name] = 1
#         print(award, nominee_name_count)
        two_presenters = [] 
        for i in range(2): 
            try:
                top_presenter = max(presenter_name_count.items(), key=operator.itemgetter(1))[0]
                two_presenters.append(top_presenter)
                del top_presenter[top_nominee]
            except: 
                two_presenters.append("")
        presenters[award] = two_presenters
        print(award,presenters[award])
        print('-----------------------------------------')
    return presenters 