import tweepy
import time
from textblob import TextBlob

consumer_key = 'UG105wh8RoCICKK3cw7Q'
consumer_secret = 'DtahmWvGvk64gkcGuMW04ddVLu82UlHffv0yKhjgMM'

access_token = '286586276-edTeXJDlptDyl7eJ4q9D4lFy3QxjD7XukUyBxv0w'
access_token_secret = 'f4QjqtJevAg5TTso44QxhyWjGSVF2vf7kqlXSlhU15CHW'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
input = raw_input('Input username: ')
input2 = raw_input('Analyse most recent ___ tweets: ')
time.sleep(2)
print 'Hold on while we fetch most recent ' + str(input2) + ' tweets...'

statuses = api.user_timeline(id = input, count = input2)
pos = 0
neg = 0

for status in statuses:
	analysis = TextBlob(status.text)
	if(analysis.sentiment.polarity>0):
		pos = pos + analysis.sentiment.polarity	
	if(analysis.sentiment.polarity<0):
		neg = neg - analysis.sentiment.polarity

print 'TL Positivity Gauge: ' + str(round( (float(pos) / float(input2) * 100), 2))
print 'TL Negativity Gauge: ' + str(round( (float(neg) / float(input2) * 100), 2))

if( float(neg) - float(pos) > 10):
	print 'This doesn\'t seem like a great time to go on Twitter :/'

