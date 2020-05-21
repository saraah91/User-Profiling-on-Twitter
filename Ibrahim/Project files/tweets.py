import tweepy

auth = tweepy.OAuthHandler('SMMEliDrPSMnCX9JkX1jDdjK5', 'JyTaaIfHgBVkOzCiutPjhh5HKAv3bCt4M4Y3dn8W8iTiDYS4cX')
auth.set_access_token('856672885-NggrT8H1xP1XA8eiV8WEkAwXNbLBAcCqUkevZu9X', 'ZWLYD0WJKjulXWX1QcMIAYSpT3qr8C0Jatim3FNy9LOOm')

api = tweepy.API(auth)
'''
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
'''
user = api.get_user('Cookie_Brho')
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)
