from app import app
import json
from flask import Flask, flash, request, redirect, url_for
from flask import render_template
import functions

#the magic happens here, when the user is at the default location, we create the object with all the needed 
#data and return a rendered html page
@app.route('/')
def doTheMagic():
    jamalTweets = functions.parseJSONTweets('jamalrayyan.jsonl')
    jamalTweets = functions.sortTweetsByRetweetCount(jamalTweets)
    resultsDict = {
        "NoOfTweets" : functions.getTweetsNumber(jamalTweets[0]),
        "NoOfFollowers" : functions.getFollowers(jamalTweets[0]),
        "NoOfFollowing" : functions.getFollowing(jamalTweets[0]),
        "NoOfListed" : functions.getListed(jamalTweets[0]),
        "NoOfRetweets" : functions.getRetweetsNumber(jamalTweets[0]),
        "UserName" : functions.getName(jamalTweets[0]),
        "UserScreenName" : functions.getScreenName(jamalTweets[0]),
        "UserDescription" : functions.getDescription(jamalTweets[0]),
        "VerifiedUser" : functions.verifiedUser(jamalTweets[0]),
        "TopLanguages" : functions.getTweetsLanguages(jamalTweets),
        "TopHashtags" : functions.getTopHashtags(jamalTweets),
        "TopLocations" : functions.getTweetsLocation(jamalTweets)
    }
    resultsJSON = json.dumps(resultsDict)
    print(resultsDict)
    print('')
    print(resultsJSON)
    return render_template('index.html')