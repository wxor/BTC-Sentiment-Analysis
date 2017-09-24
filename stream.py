import tweepy
import config
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
  
auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)
 
api = tweepy.API(auth)
   
class MyListener(StreamListener):
 
	def on_data(self, data):
		try:
			with open('bitcoin.json', 'a') as f:
				f.write(data)
			return True
		except BaseException as e:
			print("Error on_data: %s" % str(e))
		return True
 
	def on_error(self, status):
		print(status)
		return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#bitcoin', '#btc', '#cryptocoin'])
 
