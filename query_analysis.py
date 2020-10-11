import csv
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
#import Levenshtein
from pandas import DataFrame
from collections import Counter
import random




# data = {'ip': [],
#         'query': [],
#         'query_len': [],
#         'reformulation': []}
#
#
# day1 = open('day1(cleaned).csv', 'r')
# csvReader = csv.reader(day1)
# header = csvReader.next()
# urlData = header.index('request_url_query')

df = pd.read_csv('day1(cleaned).csv')
#reads .csv file
df = df.drop(columns=['remote_host', 'time_received_isoformat', 'request_method', 'time_received_isoformat', 'request_url_path', 'status', 'request_header_user_agent'])
#drops unwanted columns within .csv file
print(df.shape[0], 'before')
#prints total rows before adjustments
df = df.dropna(how='any')
#enables dropping of rows within column
df = df[~df.request_url_query.str.contains(".*?version")]
df = df[~df.request_url_query.str.contains(".*?d=")]
df = df[~df.request_url_query.str.contains(".*?aspxerrorpath")]
df = df[~df.request_url_query.str.contains(".*?404_Not_Found")]
df = df[~df.request_url_query.str.contains(".*?iSongID=")]
df = df[~df.request_url_query.str.contains(".*?iQuery=")]
df = df[~df.request_url_query.str.contains(".*?NewsMiniListing_Syndication")]
df = df[~df.request_url_query.str.contains(".*?ImageName=")]
df = df[~df.request_url_query.str.contains(".*?NewsListing_SyndicationType=1")]
df = df[~df.request_url_query.str.contains(".*?page=1&ssterms=The+Triumph+of+Fortitude+Tapestry")]
#strings that were dropped

print(df.shape[0], 'after')
#prints remaining rows that were not dropped
print(df)
#prints dataframe into console

df.groupby('request_url_query')['request_url_query'].nunique().plot(kind='bar')
#plots specfic column into a bar graph
plt.savefig('day1.png')
#saves graph as a png

#c.plot(kind='bar', title='requests')
#c.show()

#plt.plot(df['request_url_query'])
#plt.xticks(range(len(df['time_received_isoformat'])) , df['time_received_isoformat'])
#plt.show()



#print (df.head(5))
# for row in csvReader:
#     url = row[urlData]
#     print(url)
#     break

    #     print (queries)
    #     break
#         query = url['q']
#         query = query[0]
#         query = query.lower()
#         data['reformulation'].append('new')
#         data['ip'].append(line['remote_host'])
#         data['query'].append(query)
#         data['query_len'].append(len(query.split()))
#
# data = DataFrame(data)
