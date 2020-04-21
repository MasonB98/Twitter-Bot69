import tweepy
import time



CONSUMER_KEY = 'Your consumer key'
CONSUMER_SECRET = 'your consumer secret'
ACCESS_KEY = 'your access key'
ACCESS_SECRET = 'your access secret'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()

print(mentions)


#Every 69 minutes it prints 'nice'

def countdown(n):
    
    while n>0:
        old_69 = ''
        print(n)
        time.sleep(1)
        n = n-1
        if n == 0:
            api.update_status(f"Nice \n(69 minutes have passed)")
        elif n == 1:
            for i in api.user_timeline():
                old_69 = i.id
                api.destroy_status(old_69)

while True:    
    countdown(4140)

