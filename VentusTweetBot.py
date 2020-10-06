import tweepy
import datetime

consumer_key = 'aVlWZw9kp0qLAuYjYoIDzZ11B'
consumer_secret = 'OSQlz9q3UwhBOLvTXFzKyAzrtO4XyLSWKACr6YFZkHflpNL69G'
access_token = '1684919425-7Pzg1et9gsvBPmesSmrniZbaXA7tnURi85OGZZZ'
access_token_secret = 'VrJdMIsZwpcNUWdWxLJsHjdxdyzlXouP36TCUBgHKmsmW'

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
