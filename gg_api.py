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

    print("Getting Host(s) for", year, "Golden Globes")
    hosts = get_hosts(year)
    pprint(hosts)

    print("Getting Award Names")
    awards = get_awards(year)
    pprint(awards)
    
    print("Getting Nominees Names")
    nominees = get_nominees(year)
    pprint(nominees)

    print("Getting Winners Names")
    winners = get_winner(year)
    pprint(winners)
    
    print("Getting Presenters Names")
    presenters = get_presenters(year)
    pprint(presenters)

    print("Getting Redcarpet")
    max_best_dressed, best_runner_up, max_worst_dressed, worst_runner_up, max_discussed, max_controversy = get_redcarpet(year)
    pprint(redcarpet)

    # output human readable format
    readable_OFFICIAL_AWARDS_1315 = ['Cecil B. Demille Award', 'Best Motion Picture - Drama', 'Best Performance By An Actress In A Motion Picture - Drama', 'Best Performance By An Actor In A Motion Picture - Drama', 'Best Motion Picture - Comedy Or Musical', 'Best Performance By An Actress In A Motion Picture - Comedy Or Musical', 'Best Performance By An Actor In A Motion Picture - Comedy Or Musical', 'Best Animated Feature Film', 'Best Foreign Language Film', 'Best Performance By An Actress In A Supporting Role In A Motion Picture', 'Best Performance By An Actor In A Supporting Role In A Motion Picture', 'Best Director - Motion Picture', 'Best Screenplay - Motion Picture', 'Best Original Score - Motion Picture', 'Best Original Song - Motion Picture', 'Best Television Series - Drama', 'Best Performance By An Actress In A Television Series - Drama', 'Best Performance By An Actor In A Television Series - Drama', 'Best Television Series - Comedy Or Musical', 'Best Performance By An Actress In A Television Series - Comedy Or Musical', 'Best Performance By An Actor In A Television Series - Comedy Or Musical', 'Best Mini-series Or Motion Picture Made For Television', 'Best Performance By An Actress In A Mini-series Or Motion Picture Made For Television', 'Best Performance By An Actor In A Mini-series Or Motion Picture Made For Television', 'Best Performance By An Actress In A Supporting Role In A Series, Mini-series Or Motion Picture Made For Television', 'Best Performance By An Actor In A Supporting Role In A Series, Mini-series Or Motion Picture Made For Television']
    readable_OFFICIAL_AWARDS_1819 = ['Best Motion Picture - Drama', 'Best Motion Picture - Musical Or Comedy', 'Best Performance By An Actress In A Motion Picture - Drama', 'Best Performance By An Actor In A Motion Picture - Drama', 'Best Performance By An Actress In A Motion Picture - Musical Or Comedy', 'Best Performance By An Actor In A Motion Picture - Musical Or Comedy', 'Best Performance By An Actress In A Supporting Role In Any Motion Picture', 'Best Performance By An Actor In A Supporting Role In Any Motion Picture', 'Best Director - Motion Picture', 'Best Screenplay - Motion Picture', 'Best Motion Picture - Animated', 'Best Motion Picture - Foreign Language', 'Best Original Score - Motion Picture', 'Best Original Song - Motion Picture', 'Best Television Series - Drama', 'Best Television Series - Musical Or Comedy', 'Best Television Limited Series Or Motion Picture Made For Television', 'Best Performance By An Actress In A Limited Series Or A Motion Picture Made For Television', 'Best Performance By An Actor In A Limited Series Or A Motion Picture Made For Television', 'Best Performance By An Actress In A Television Series - Drama', 'Best Performance By An Actor In A Television Series - Drama', 'Best Performance By An Actress In A Television Series - Musical Or Comedy', 'Best Performance By An Actor In A Television Series - Musical Or Comedy', 'Best Performance By An Actress In A Supporting Role In A Series, Limited Series Or Motion Picture Made For Television', 'Best Performance By An Actor In A Supporting Role In A Series, Limited Series Or Motion Picture Made For Television', 'Cecil B. Demille Award']

    awards = readable_OFFICIAL_AWARDS_1819
    if year in [2013, 2015]:
        awards = readable_OFFICIAL_AWARDS_1315
    
    pprint("Golden Globes", year, "Award Results:")
    pprint("Host(s):", convert_human_readable_list(hosts))
    pprint("\n")
    for award in awards:
        key = award.lower()
        pprint("Award:", award)
        pprint("Presenters:", convert_human_readable_list(presenters[key]))
        pprint("Nominees:", convert_human_readable_list(nominees[key]))
        pprint("Winner:", convert_human_readable_list(winners[key]))
        pprint("\n")

    pprint("Our Parsed Awards:", convert_human_readable_list(awards))

    pprint("Red Carpet")
    pprint("Best Dressed:", max_best_dressed)
    pprint("Best Dressed Runner Up:", best_runner_up)
    pprint("Worst Dressed:", max_worst_dressed)
    pprint("Worst Dressed Runner Up:", worst_runner_up)
    pprint("Most Discussed:", max_discussed)
    pprint("Most Controversial:", max_controversy)

    # output autograder JSON format
    autograder_json = {}
    autograder_json["Host"] = hosts
    for award in awards: 
        key = award.lower()
        award_category = {}
        award_category["Presenters"] = presenters[key]
        award_category["Nominees"] = nominees[key]
        award_category["Winner"] = winner[key]
        autograder_json[award] = award_category
    return autograder_json

    fin = input("Press enter to exit")
    return

if __name__ == '__main__':
    main()
