import tweepy
import datetime

consumer_key = '' #enter your consumer key here
consumer_secret = '' #enter your consumer secret key here
access_token = '' #enter your access token here
access_token_secret = '' #enter your access token secret here

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def publictweet():
    if datetime.date.today().weekday() == 0:
        tweettopublish = 'Hi everyone, today is Monday. #Monday #Bot'
    if datetime.date.today().weekday() == 1:
        tweettopublish = 'Enjoy your Tuesday. #Tueday #Bot'
    if datetime.date.today().weekday() == 2:
        tweettopublish = 'Third day of the week. #Wednesday #Bot'
    if datetime.date.today().weekday() == 3:
        tweettopublish = 'Fourth day of the week. #Thursday #Bot'
    if datetime.date.today().weekday() == 4:
        tweettopublish = 'Fifth day of the week. #Friday #Bot'
    if datetime.date.today().weekday() == 5:
        tweettopublish = 'Sixth day of the week. #Saturday #Bot'
    if datetime.date.today().weekday() == 6:
        tweettopublish = 'Seventh day of the week. #Sunday #Bot'

    api.update_status(tweettopublish)
    print(tweettopublish)
    print(datetime.date.today().weekday())


publictweet()
