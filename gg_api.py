'''Version 0.35'''
# python library imports
import time
import nltk
from pprint import pprint
import os.path
import json
from os import path

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
    hosts = []

    global PATH_TO_DATASET

    print("Retrieving Hosts")
    filename = 'cache/'+str(year)+'results.json'
    if path.exists(filename):
        with open(filename, 'r', encoding='utf8') as f:
            json_cache = json.load(f)
            hosts = json_cache['hosts']
    else:
        data = get_tweets(year, PATH_TO_DATASET, ALL_TWEETS)
        hosts = _get_hosts(year, data)
    return hosts

def get_awards(year):
    '''Awards is a list of strings. Do NOT change the name
    of this function or what it returns.'''
    # Your code here
    awards = []

    global PATH_TO_DATASET
    
    data = get_tweets(year, PATH_TO_DATASET, ALL_TWEETS)

    print("Retrieving Awards...")
    filename = 'cache/'+str(year)+'results.json'
    if path.exists(filename):
        with open(filename, 'r', encoding='utf8') as f:
            json_cache = json.load(f)
            awards = json_cache['awards']
    else:
        awards = _get_awards(data)

    return awards

def get_nominees(year):
    '''Nominees is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change
    the name of this function or what it returns.'''
    # Your code here
    nominees = {}
    print("Retrieving Nominees...")
    filename = 'cache/'+str(year)+'results.json'
    if path.exists(filename):
        with open(filename, 'r', encoding='utf8') as f:
            json_cache = json.load(f)
            nominees = json_cache['nominees']
    else:
        global PATH_TO_DATASET

        global OFFICIAL_AWARDS_1315
        global OFFICIAL_AWARDS_1819
        awards = OFFICIAL_AWARDS_1819

        if year in [2013, 2015]:
            awards = OFFICIAL_AWARDS_1315

        # print("Loading Golden Globes dataset from", year)
        data = get_tweets(year, PATH_TO_DATASET, ALL_TWEETS)
        # print("Done loading dataset") 

        
        nominees = _get_nominees(data, awards)
    
    return nominees

def get_winner(year):
    '''Winners is a dictionary with the hard coded award
    names as keys, and each entry containing a single string.
    Do NOT change the name of this function or what it returns.'''
    # Your code here
    winners = {}
    print("Retrieving Winners...")
    filename = 'cache/'+str(year)+'results.json'
    if path.exists(filename):
        with open(filename, 'r', encoding='utf8') as f:
            json_cache = json.load(f)
            winners = json_cache['winners']
    else:
        global PATH_TO_DATASET

        global OFFICIAL_AWARDS_1315
        global OFFICIAL_AWARDS_1819
        awards = OFFICIAL_AWARDS_1819

        if year in [2013, 2015]:
            awards = OFFICIAL_AWARDS_1315

        # print("Loading Golden Globes dataset from", year)
        data = get_tweets(year, PATH_TO_DATASET, ALL_TWEETS)
        # print("Done loading dataset") 

        
        winners = _get_winner(data, awards)

    return winners

def get_presenters(year):
    '''Presenters is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change the
    name of this function or what it returns.'''
    # Your code here
    presenters = {}
    print("Retrieving Presenters...")
    filename = 'cache/'+str(year)+'results.json'
    if path.exists(filename):
        with open(filename, 'r', encoding='utf8') as f:
            json_cache = json.load(f)
            presenters = json_cache['presenters']
    else:
        global PATH_TO_DATASET

        global OFFICIAL_AWARDS_1315
        global OFFICIAL_AWARDS_1819
        awards = OFFICIAL_AWARDS_1819
        
        # print("Loading Golden Globes dataset from", year)
        data = get_tweets(year, PATH_TO_DATASET, ALL_TWEETS)
        # print("Done loading dataset") 

        if year in [2013, 2015]:
            awards = OFFICIAL_AWARDS_1315
        
        
        presenters = _get_presenters(data, awards)
    return presenters

def get_redcarpet(year):
    redcarpet = []
    filename = 'cache/'+str(year)+'results.json'
    if path.exists(filename):
        with open(filename, 'r', encoding='utf8') as f:
            json_cache = json.load(f)
            redcarpet = json_cache['redcarpet']
    else:
        global PATH_TO_DATASET
        
        # print("Loading Golden Globes dataset from", year)
        data = get_tweets(year, PATH_TO_DATASET, ALL_TWEETS)
        # print("Done loading dataset") 

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

    filename = 'cache/'+str(year)+'results.json'
    
    if path.exists(filename):
        with open(filename, 'r', encoding='utf8') as f:
            json_cache = json.load(f)
            
            # primary goals
            hosts = json_cache["hosts"]
            awards = json_cache["awards"]
            nominees = json_cache["nominees"]
            winners = json_cache["winners"]
            presenters = json_cache["presenters"]
            # presenters = get_presenters(year)
            # print(presenters)

            redcarpet = json_cache["redcarpet"]
            max_best_dressed = redcarpet[0]
            best_runner_up = redcarpet[1]
            max_worst_dressed = redcarpet[2]
            worst_runner_up = redcarpet[3]
            max_discussed = redcarpet[4]
            max_controversy = redcarpet[5]

    else:
        json_cache = {}

        print("Getting Host(s) for", year, "Golden Globes")
        hosts = get_hosts(year)
        json_cache["hosts"] = hosts
        # pprint(hosts)

        print("Getting Award Names")
        awards = get_awards(year)
        json_cache["awards"] = awards
        # pprint(awards)
        
        print("Getting Nominees Names")
        nominees = get_nominees(year)
        json_cache["nominees"] = nominees
        # pprint(nominees)

        print("Getting Winners Names")
        winners = get_winner(year)
        json_cache["winners"] = winners
        # pprint(winners)
        
        print("Getting Presenters Names")
        presenters = get_presenters(year)
        json_cache["presenters"] = presenters
        # pprint(presenters)

        print("Getting Redcarpet")
        max_best_dressed, best_runner_up, max_worst_dressed, worst_runner_up, max_discussed, max_controversy = get_redcarpet(year)
        redcarpet = [max_best_dressed, best_runner_up, max_worst_dressed, worst_runner_up, max_discussed, max_controversy]
        json_cache["redcarpet"] = redcarpet

        with open(filename, 'w') as fp:
            json.dump(json_cache, fp)


 
    # output human readable format
    readable_OFFICIAL_AWARDS_1315 = ['Cecil B. Demille Award', 'Best Motion Picture - Drama', 'Best Performance By An Actress In A Motion Picture - Drama', 'Best Performance By An Actor In A Motion Picture - Drama', 'Best Motion Picture - Comedy Or Musical', 'Best Performance By An Actress In A Motion Picture - Comedy Or Musical', 'Best Performance By An Actor In A Motion Picture - Comedy Or Musical', 'Best Animated Feature Film', 'Best Foreign Language Film', 'Best Performance By An Actress In A Supporting Role In A Motion Picture', 'Best Performance By An Actor In A Supporting Role In A Motion Picture', 'Best Director - Motion Picture', 'Best Screenplay - Motion Picture', 'Best Original Score - Motion Picture', 'Best Original Song - Motion Picture', 'Best Television Series - Drama', 'Best Performance By An Actress In A Television Series - Drama', 'Best Performance By An Actor In A Television Series - Drama', 'Best Television Series - Comedy Or Musical', 'Best Performance By An Actress In A Television Series - Comedy Or Musical', 'Best Performance By An Actor In A Television Series - Comedy Or Musical', 'Best Mini-series Or Motion Picture Made For Television', 'Best Performance By An Actress In A Mini-series Or Motion Picture Made For Television', 'Best Performance By An Actor In A Mini-series Or Motion Picture Made For Television', 'Best Performance By An Actress In A Supporting Role In A Series, Mini-series Or Motion Picture Made For Television', 'Best Performance By An Actor In A Supporting Role In A Series, Mini-series Or Motion Picture Made For Television']
    readable_OFFICIAL_AWARDS_1819 = ['Best Motion Picture - Drama', 'Best Motion Picture - Musical Or Comedy', 'Best Performance By An Actress In A Motion Picture - Drama', 'Best Performance By An Actor In A Motion Picture - Drama', 'Best Performance By An Actress In A Motion Picture - Musical Or Comedy', 'Best Performance By An Actor In A Motion Picture - Musical Or Comedy', 'Best Performance By An Actress In A Supporting Role In Any Motion Picture', 'Best Performance By An Actor In A Supporting Role In Any Motion Picture', 'Best Director - Motion Picture', 'Best Screenplay - Motion Picture', 'Best Motion Picture - Animated', 'Best Motion Picture - Foreign Language', 'Best Original Score - Motion Picture', 'Best Original Song - Motion Picture', 'Best Television Series - Drama', 'Best Television Series - Musical Or Comedy', 'Best Television Limited Series Or Motion Picture Made For Television', 'Best Performance By An Actress In A Limited Series Or A Motion Picture Made For Television', 'Best Performance By An Actor In A Limited Series Or A Motion Picture Made For Television', 'Best Performance By An Actress In A Television Series - Drama', 'Best Performance By An Actor In A Television Series - Drama', 'Best Performance By An Actress In A Television Series - Musical Or Comedy', 'Best Performance By An Actor In A Television Series - Musical Or Comedy', 'Best Performance By An Actress In A Supporting Role In A Series, Limited Series Or Motion Picture Made For Television', 'Best Performance By An Actor In A Supporting Role In A Series, Limited Series Or Motion Picture Made For Television', 'Cecil B. Demille Award']

    official_awards = readable_OFFICIAL_AWARDS_1819
    if year in [2013, 2015]:
        official_awards = readable_OFFICIAL_AWARDS_1315
    
    print("Golden Globes Award Results for", year)
    print('\n')
    print("Host(s):", convert_human_readable_list(hosts))
    print('\n')
    for award in official_awards:
        key = award.lower()
        print("Award:", award)
        # print("Presenters:", convert_human_readable_list(presenters[key]))
        print("Nominees:", convert_human_readable_list(nominees[key]))
        print("Winner:", winners[key])
        print('\n')

    print("Our Parsed Awards:", convert_human_readable_list(awards))

    print("Red Carpet")
    print("Best Dressed:", max_best_dressed)
    print("Best Dressed Runner Up:", best_runner_up)
    print("Worst Dressed:", max_worst_dressed)
    print("Worst Dressed Runner Up:", worst_runner_up)
    print("Most Discussed:", max_discussed)
    print("Most Controversial:", max_controversy)
    print('\n')

    autograder_json = {}
    autograder_json["Host"] = hosts
    for award in official_awards: 
        key = award.lower()
        award_category = {}
        award_category["Presenters"] = presenters[key]
        award_category["Nominees"] = nominees[key]
        award_category["Winner"] = winners[key]
        autograder_json[award] = award_category

    return autograder_json

if __name__ == '__main__':
    main()
