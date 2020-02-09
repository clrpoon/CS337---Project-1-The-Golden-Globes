# python library imports
import json
import time

# local files imports
from gg_api import ALL_TWEETS

def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)


def get_tweets(year, path_to_dataset):
    global ALL_TWEETS

    if year in ALL_TWEETS:
        return ALL_TWEETS[year]
    else:
        try:
            file = open(path_to_dataset+'gg'+str(year)+'.json', encoding = 'utf8')
            data = json.load(file)

            ALL_TWEETS[year] = [line['text'] for line in data]
            return ALL_TWEETS[year]
        except:
            print('could not read json in the form of dictionary list')
            print('trying jsonl reading instead')
        try:
            with open(path_to_dataset+'gg'+str(year)+'.json', encoding='utf8') as f:
                lines = f.readlines()

            gg_data = []
            for line in lines:
                gg_data.append(json.loads(line)['text'])

            ALL_TWEETS[year] = gg_data
            return ALL_TWEETS[year]
        except:
            print('could not read json as jsonl')
            print('get_tweets returned []')
        return []


def load_all(path_to_dataset, show_performance = False):
    if show_performance:
        init_time = time.time()
        
        start_time = time.time()
        print('loading gg2013.json start time', convert(start_time))
        get_tweets(2013, path_to_dataset)
        end_time = time.time()
        print('loading gg2013.json end time', convert(end_time))
        elapsed_time = time.time() - start_time
        print('time elapsed', convert(elapsed_time))
    
        
        start_time = time.time()
        print('loading gg2015.json start time', convert(start_time))
        get_tweets(2015, path_to_dataset)
        end_time = time.time()
        print('loading gg2015.json end time', convert(end_time))
        elapsed_time = time.time() - start_time
        print('time elapsed', convert(elapsed_time))
        
        start_time = time.time()
        print('loading gg2020.json start time', convert(start_time))
        get_tweets(2020, path_to_dataset)
        end_time = time.time()
        print('loading gg2020.json end time', convert(end_time))
        elapsed_time = time.time() - start_time
        print('time elapsed', convert(elapsed_time))
        
        print('total time elapsed', time.time() - init_time)
    else:
        print('loading gg2013.json')
        get_tweets(2013, path_to_dataset)
        print('gg2013 done loading')
        
        print('loading gg2015.json')
        get_tweets(2015, path_to_dataset)
        print('gg2015 done loading')

        print('loading gg2020.json')
        get_tweets(2020, path_to_dataset)
        print('gg2020 done loading')