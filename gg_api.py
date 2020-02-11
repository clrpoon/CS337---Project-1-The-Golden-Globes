'''Version 0.35'''
# python library imports
import time
import nltk
from pprint import pprint

# local file imports
from util import *
from load_data import *

# imports for each function
from get_hosts import _get_hosts
from get_awards import _get_awards
from get_nominees import _get_nominees
from get_winner import _get_winner
from get_presenters import _get_presenters
from get_redcarpet import _get_redcarpet

OFFICIAL_AWARDS_1315 = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']
OFFICIAL_AWARDS_1819 = ['best motion picture - drama', 'best motion picture - musical or comedy', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best performance by an actress in a motion picture - musical or comedy', 'best performance by an actor in a motion picture - musical or comedy', 'best performance by an actress in a supporting role in any motion picture', 'best performance by an actor in a supporting role in any motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best motion picture - animated', 'best motion picture - foreign language', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best television series - musical or comedy', 'best television limited series or motion picture made for television', 'best performance by an actress in a limited series or a motion picture made for television', 'best performance by an actor in a limited series or a motion picture made for television', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best performance by an actress in a television series - musical or comedy', 'best performance by an actor in a television series - musical or comedy', 'best performance by an actress in a supporting role in a series, limited series or motion picture made for television', 'best performance by an actor in a supporting role in a series, limited series or motion picture made for television', 'cecil b. demille award']
# PATH_TO_DATASET = ""
PATH_TO_DATASET = "../gg-datasets/"
ALL_TWEETS = {}

def get_hosts(year):
    '''Hosts is a list of one or more strings. Do NOT change the name
    of this function or what it returns.'''
    # Your code here
    global PATH_TO_DATASET
    
    print("Loading Golden Globes dataset from", year)
    data = get_tweets(year, PATH_TO_DATASET, ALL_TWEETS)
    print("Done loading dataset") 

    print("Retrieving Hosts")
    hosts = _get_hosts(year, data)
    return hosts

def get_awards(year):
    '''Awards is a list of strings. Do NOT change the name
    of this function or what it returns.'''
    # Your code here
    global PATH_TO_DATASET
    
    print("Loading Golden Globes dataset from", year)
    data = get_tweets(year, PATH_TO_DATASET, ALL_TWEETS)
    print("Done loading dataset") 

    print("Retrieving Awards...")
    awards = _get_awards(data)

    return awards

def get_nominees(year):
    '''Nominees is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change
    the name of this function or what it returns.'''
    # Your code here
    global PATH_TO_DATASET

    global OFFICIAL_AWARDS_1315
    global OFFICIAL_AWARDS_1819
    awards = OFFICIAL_AWARDS_1819

    if year in [2013, 2015]:
        awards = OFFICIAL_AWARDS_1315

    print("Loading Golden Globes dataset from", year)
    data = get_tweets(year, PATH_TO_DATASET, ALL_TWEETS)
    print("Done loading dataset") 

    print("Retrieving Nominees...")
    nominees = _get_nominees(data, awards)
    
    return nominees

def get_winner(year):
    '''Winners is a dictionary with the hard coded award
    names as keys, and each entry containing a single string.
    Do NOT change the name of this function or what it returns.'''
    # Your code here
    global PATH_TO_DATASET

    global OFFICIAL_AWARDS_1315
    global OFFICIAL_AWARDS_1819
    awards = OFFICIAL_AWARDS_1819

    if year in [2013, 2015]:
        awards = OFFICIAL_AWARDS_1315

    print("Loading Golden Globes dataset from", year)
    data = get_tweets(year, PATH_TO_DATASET, ALL_TWEETS)
    print("Done loading dataset") 

    print("Retrieving Winners")
    winners = _get_winner(data, awards)

    return winners

def get_presenters(year):
    '''Presenters is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change the
    name of this function or what it returns.'''
    # Your code here
    global PATH_TO_DATASET

    global OFFICIAL_AWARDS_1315
    global OFFICIAL_AWARDS_1819
    awards = OFFICIAL_AWARDS_1819
    
    print("Loading Golden Globes dataset from", year)
    data = get_tweets(year, PATH_TO_DATASET, ALL_TWEETS)
    print("Done loading dataset") 

    if year in [2013, 2015]:
        awards = OFFICIAL_AWARDS_1315
    
    print("Retrieving Presenters...")
    presenters = _get_presenters(data, awards)
    return presenters

def get_redcarpet(year):
    global PATH_TO_DATASET
    
    print("Loading Golden Globes dataset from", year)
    data = get_tweets(year, PATH_TO_DATASET, ALL_TWEETS)
    print("Done loading dataset") 

    if year in [2013, 2015]:
        awards = OFFICIAL_AWARDS_1315

    redcarpert = _get_redcarpet(data, year)
    
    return redcarpert

def pre_ceremony():
    '''This function loads/fetches/processes any data your program
    will use, and stores that data in your DB or in a json, csv, or
    plain text file. It is the first thing the TA will run when grading.
    Do NOT change the name of this function or what it returns.'''
    # Your code here
    # load_all(PATH_TO_DATASET)
    nltk.download('wordnet')
    nltk.download('stopwords')
    print("Pre-ceremony processing complete.")
    return

def main():
    '''This function calls your program. Typing "python gg_api.py"
    will run this function. Or, in the interpreter, import gg_api
    and then run gg_api.main(). This is the second thing the TA will
    run when grading. Do NOT change the name of this function or
    what it returns.'''
    # Your code here
    global PATH_TO_DATASET
    global ALL_TWEETS
    # PATH_TO_DATASET = "../gg-datasets/"
    # PATH_TO_DATASET = input("Please enter filepath to Golden Globe Dataset Golden Globes Dataset:\n")

    pre_ceremony()
    year = int(input("Please enter year of Golden Globes Dataset:\n"))

    # print("Getting Host(s) for", year, "Golden Globes")
    # hosts = get_hosts(year)
    # pprint(hosts)

    # print("Getting Award Names")
    # awards = get_awards(year)
    # pprint(awards)
    
    print("Getting Nominees Names")
    nominees = get_nominees(year)
    pprint(nominees)

    # print("Getting Winners Names")
    # winners = get_winner(year)
    # pprint(winners)
    
    # print("Getting Presenters Names")
    # presenters = get_presenters(year)
    # pprint(presenters)

    # print("Getting Redcarpet")
    # redcarpet = get_redcarpet(year)
    # pprint(redcarpet)
   

    fin = input("Press enter to exit")
    return

if __name__ == '__main__':
    main()
