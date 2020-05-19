import json
from collections import OrderedDict
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory

def parseJSONTweets(fileName):
    tweets = []
    with open (fileName, "r") as f:
        for line in f:
            tweet = json.loads(line)
            tweets.append(tweet)   
    return tweets

tweets = parseJSONTweets('artweets.json')
jamalTweets = parseJSONTweets('jamalrayyan.jsonl')

#sorts tweets according to which tweet has the most retweets
#input: list of tweets, output: list of sorted tweets
def sortTweetsByRetweetCount(tweets):
    sortedTweets = sorted(tweets, key=lambda k: k['retweet_count'], reverse=True) 
    return sortedTweets

#sorts tweets according to most recent tweet
#input: list of tweets, output: list of sorted tweets
def sortTweetsByMostRecent(tweets):
    sortedTweets = sorted(tweets, key=lambda k: k['created_at'], reverse=True) 
    return sortedTweets

#get the number of followers of the tweet's user 
#input: one tweet, output: int number of followers
def getFollowers(tweet):
    return tweet['user']['followers_count']

#get the number of following of the tweet's user
#input: one tweet, output: int number of followed users
def getFollowing(tweet):
    return tweet['user']['friends_count']

#get the number of listed of the tweet's user
#input: one tweet, output: int number of listed users
def getListed(tweet):
    return tweet['user']['listed_count']

#get the number of tweets of the tweet's user
#input: one tweet, output: int number of total tweets
def getTweetsNumber(tweet):
    return tweet['user']['statuses_count']

#get the number of retweets of the tweet
#input: one tweet, output: int number of total retweets
def getRetweetsNumber(tweet):
    return tweet['retweet_count']

#get the name of the tweet's user
#input: one tweet, output: string name 
def getName(tweet):
    return tweet['user']['name']

#get the screen name of the tweet's user
#input: one tweet, output: string screen name 
def getScreenName(tweet):
    return tweet['user']['screen_name']

#check if the tweet's user is verified 
#input: one tweet, output: true/false
def verifiedUser(tweet):
    if tweet['user']['verified'] == 'True':
        return True

#get the description of the tweet's user
#input: one tweet, output: string description 
def getDescription(tweet):
    return tweet['user']['description']

#get the top hundred used hashtags used in a list of tweets
#input: list of tweets, output: dict of sorted tweets
def getTopHashtags(tweets):
    topHashtags = {}
    HIGHEST_HASHTAGS = 100
    for tweet in tweets:
        for hashtag in tweet['entities']['hashtags']:
            one_hashtag = [hashtag['text']]
            if one_hashtag[0] in topHashtags:
                topHashtags[one_hashtag[0]] = topHashtags[one_hashtag[0]] +1
            else:
                topHashtags[one_hashtag[0]] = 1
    topHashtags = OrderedDict(sorted(topHashtags.items(),key=lambda x: x[1], reverse=True))
    topHundredHashtags = dict(list(topHashtags.items())[0:HIGHEST_HASHTAGS])
    return topHundredHashtags

#get the top locations tweets came from
#input: list of tweets, output: dict of sorted tweets
def getTweetsLocation(tweets):
    topLocations = {}
    HIGHEST_LOCATIONS = 10
    for tweet in tweets:
        location = tweet['user']['location']
        one_location = [location]
        if  one_location[0] in  topLocations:
                topLocations[one_location[0]] = topLocations[one_location[0]] +1
        else:
            topLocations[one_location[0]] = 1
    topLocations = OrderedDict(sorted(topLocations.items(),key=lambda x: x[1], reverse=True))
    highestLocations = dict(list(topLocations.items())[0:HIGHEST_LOCATIONS])
    return highestLocations

def getTweetsLanguages(tweets):
    topLanguages = {}
    TOP_USED_LANGUAGES = 10
    for tweet in tweets:
        language = tweet['lang']
        one_language = [language]
        if  one_language[0] in topLanguages:
            topLanguages[one_language[0]] = topLanguages[one_language[0]] +1
        else:
            topLanguages[one_language[0]] = 1
    topLanguages = OrderedDict(sorted(topLanguages.items(),key=lambda x: x[1], reverse=True))
    highestLanguages = dict(list(topLanguages.items())[0:TOP_USED_LANGUAGES])
    return highestLanguages

'''
for key,val in jamalTweets[1].items():
    print(key, "=>", val)
print('\n')
for key,val in jamalTweets[1]['user'].items():
    print(key, "=>", val)
print('\n')
for key,val in jamalTweets[1]['entities'].items():
    print(key, "=>", val)
'''

# doing random tests to check if functions are working
#sortedTweets = sortTweetsByRetweetCount(tweets)
#sortedTweets = sortTweetsByMostRecent(tweets)
print('\n')
print('User Name:', getName(tweets[0]))
print('User Screen Name:', getScreenName(tweets[0]))
print('Nmber of Following:', getFollowing(tweets[0]))
print('Nmber of Followers:', getFollowers(tweets[0]))
print('Nmber of Listed:', getListed(tweets[0]))
print('Nmber of Tweets:', getTweetsNumber(tweets[0]))
print('Nmber of Retweets:', getRetweetsNumber(tweets[0]))
print('User Description:', getDescription(tweets[0]))
if verifiedUser(tweets[0]):
    print('User is Verified')
else: 
    print('User is Not Verified')
print('\n')

'''
print('Top Hashtags:')
topHundredHashtags = getTopHashtags(jamalTweets)
for key, value in topHundredHashtags.items():
    print(key, ' : ', value)
'''
print('Top Locations:')
highestLocations = getTweetsLocation(tweets)
for key, value in highestLocations.items():
        percent = value * 100 / len(tweets)
        if key == '':
            key = 'No Location Detected'
        print('{} : {}% ({} Tweets)'.format(key, str(percent)[:4], value))

print('\n')

print('Top Languages:')
highestLanguages = getTweetsLanguages(jamalTweets)
for key, value in highestLanguages.items():
        percent = value * 100 / len(jamalTweets)
        print('{} : {}% ({} Tweets)'.format(key, str(percent)[:4], value))
