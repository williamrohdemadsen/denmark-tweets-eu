import pandas as pd
import twint
import time
from multiprocessing.dummy import Pool as ThreadPool

# Load data
#get_data = pd.read_csv("py/get_data_all.csv")

# Set up twint function
def get_tweets(search):

    c = twint.Config()
    c.Search = search
    c.Lang = "dk"
    #c.Limit = 50000
    #c.Since = since
    #c.Until = until
    c.Store_csv = True
    c.Output = "data-raw/tweets_raw.csv"
    c.Hide_output = True

    twint.run.Search(c)

    #print("row " + row_no)

    time.sleep(2)


start = time.perf_counter()

get_tweets("#eudk")

# Convert dataframe to tuples
#records = get_data.to_records(index=False)
#tuples = list(records)

# Get tweets in parallel
#pool = ThreadPool(10)
#pool.starmap(get_tweets, tuples)
#pool.close()
#pool.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
