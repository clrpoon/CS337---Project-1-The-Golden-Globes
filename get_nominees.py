from util import *

def _get_nominees(tweet_list, award_list):
    nominees = dict.fromkeys(award_list)
    return nominees