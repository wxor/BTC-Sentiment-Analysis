import sentiments
import time
import datetime
import os
import config

timeout = time.time() + config.sTime
while True:
	print "Collecting data for ", config.sTime, " seconds..."
	os.remove('bitcoin.json')
	
	time.sleep(config.sTime)
	if time.time() > timeout:
		data = sentiments.main('bitcoin.json')
		sentiment, tUsed, tTotal = (data)
		print "#################################################################"
		print 'Timestamp: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())
		print "Sentiment is:",sentiment
		print "Tweets used:",tUsed
		print "Total tweets",tTotal
		print "#################################################################"
		