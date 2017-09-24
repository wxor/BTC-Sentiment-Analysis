import re
import sys
import json

def get_sent(tweet_dict, weights):
    score = 0.0
    text = ""
    if u'text' in tweet_dict:
        utf8_text = tweet_dict[u'text']
        text = utf8_text
        toks = re.split('\s+', utf8_text.lower())
        for word in toks:
            word = re.sub('\W', '', word)
            if word in weights:
                score += weights[word]
        score = min(5, score)
        score = max(-5, score)
        for word in toks:
            word = re.sub('\W', '', word)
            if word not in weights and len(word) > 3:
                weights[word] = 0

    return score, text

def readWeights():
    weights = {}
    with open('sentiments.txt') as f:
        for line in f:
            toks = re.split('\s+', line.strip().lower()) 
            if len(toks) == 2:
                word = toks[0]
                word = re.sub('\W', '', word)
                weights[word] = float(toks[1])
    return weights

def main(tweet_file):
    tc = 0
    weights = readWeights()
    sentiments = []
    with open(tweet_file) as tf:
        for line in tf:
            tc = tc+1
            if line:
                tweet = json.loads(line)
                score, tweet_text = get_sent(tweet, weights)
                sentiments.append(score)
    total = 0.0
    for num in sentiments:
        total += num
		
    ss = total / len(sentiments)
    tu = total

    return (ss,tu,tc)
	
if __name__ == '__main__':
    main(sys.argv[1])
