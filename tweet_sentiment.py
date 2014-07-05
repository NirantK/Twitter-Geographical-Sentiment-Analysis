import sys, json

def readSentiment(sent_file):
	afinnfile = open(sent_file)
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.
	return scores

def getScore(term, sent_file):
	scores = readSentiment(sent_file)
	try:
	  	return scores[term]
 	except KeyError:
  		return 0 
 
def readData(tweet_file, sent_file):
	oFile = open(tweet_file)

	for line in oFile:
		pyResponse = json.loads(line)
		try:
			pyResponse["delete"]
		except:
			result = pyResponse
			try:
				tweet =  result['text'].encode('utf-8')
			except:
				pass
			score = 0
			words = tweet.split(" ")
			for word in words:
				score +=getScore(word, sent_file)
			print score
	

def main():
    sent_file = str(sys.argv[1])
    tweet_file = str(sys.argv[2])
    readData(tweet_file,sent_file)

if __name__ == '__main__':
    main()
