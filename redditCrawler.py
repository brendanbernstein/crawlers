import csv

import requests
import json
import time
# from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

# Set your header according to the form below
# :: (by /u/)

# Add your username below
hdr = {'User-Agent': 'brendanb22'}
url = 'https://www.reddit.com/r/ethereum/.json'
req = requests.get(url, headers=hdr)
csvFile = open('reddit4.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
json_data = json.loads(req.text)
data_all = json_data['data']['children']

num_of_posts = 0
for x in data_all:
    csvWriter.writerow([time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(x['data']['created'])), x['data']['title']])
    num_of_posts +=1

while len(data_all) <= 5000:
    time.sleep(2)
    last = data_all[-1]['data']['name']
    url = 'https://www.reddit.com/r/ethereum/.json?after=' + str(last)
    req = requests.get(url, headers=hdr)
    data = json.loads(req.text)
    data_all += data['data']['children']
    for x in data['data']['children']:
        csvWriter.writerow([time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(x['data']['created'])), x['data']['title']])
