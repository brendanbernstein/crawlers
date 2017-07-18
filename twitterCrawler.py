import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'Jl8vDABDCl5LgnHtTmGBk80Zh'
consumer_secret = '5BizF08hJQaU5nuZ2AGhegyGPGhpc55LstZ9riXLfguTgoGtmn'
access_token = '243259110-LsJ7IAv8q31o1jhgxkpQAdPRd4tooaqKT8skpAh1'
access_token_secret = 'pHzCpfJ06L4NKLG2PKkxrnHo1hKtTwhtM5zGtEkjHsGwm'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
csvFile = open('ub.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="ethereum -filter:retweets",
                           lang="en",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])