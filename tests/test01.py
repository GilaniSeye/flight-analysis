from google_flight_analysis.scrape import *
import pandas as pd
#from google_flight_analysis.cache import *
# Try to keep the dates in format YYYY-mm-dd
result = Scrape('YUL', 'DSS', '2023-07-05', '2023-09-10') # obtain our scrape object

dataframe = result.data # outputs a Pandas DF with flight prices/info
origin = result.origin # 'YUL'
dest = result.dest # 'DSS'
date_leave = result.date_leave # '2023-07-05'
date_return = result.date_return # '2023-09-10'