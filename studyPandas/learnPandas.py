import pandas as pd
import urllib.request
import csv

url = 'https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/hacker_news.csv'

urllib.request.urlretrieve(url, "hacker_news.csv")

df = pd.read_csv('hacker_news.csv')

data = df['title']

print(data[data.str.contains('python')])

print(data[data.str.contains('JavaScript')])