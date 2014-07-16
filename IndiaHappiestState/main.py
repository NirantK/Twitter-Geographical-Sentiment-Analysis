import sys, json, collections

'''Written by Nirant Kasliwal, Undergraduate Information Systems Student at BITS Pilani
* Interested in Data Science
* Email: nirant[]bits[at]gmail[ dot]com'''

happyStates = {}

words_to_ignore = ["to","are","for","we","of", "@", "&amp",
 "on", "my", "at", "it", "our","they", "he", "so", 
 "the","in","a", "is", "and" ,"that","what","you","u","r",
 "with","this","would","from","your","which","hai", "", " "
 "while","these"]

things_to_strip = [".","http","t.co" ,"-",",","?",")","(","\"",":",";","'s"]

class happyState(object):
    '''Sorts tweets as per states and creates a dict of the objects'''
    def __init__(self):
        self.stateName = ""
        self.count = 0
        self.score = 0.0
        self.tweet = ""

    def setName(self, name):
        self.stateName = name

    def updateCount(self):
        self.count += 1.0

    def updateScore(self, newScore):
        self.score += newScore

    def stateSort(self, data):
        for i in xrange(len(data)):
            key = data[i].getstate()
            # replace the try except conditions with if-else
            if not key in happyStates.keys():
                happyStates[key] = happyState()
                happyStates[key].stateName = key                
            happyStates[key].score += data[i].getScore()
            happyStates[key].updateCount()
            happyStates[key].tweet += "\t" + data[i].getTweet()
            # print data[i].getTweet()
                
class Tweet:
    '''Stores the necessary data for each tweet'''
    def __init__(self):
        self.tweet = ""
        self.state = ""
        self.score = 0.0

    def setState(self, state):
        self.state = state

    def setTweet(self, tweet):
        self.tweet = tweet

    def setScore(self, score):
        self.score = score

    def getTweet(self):
        return self.tweet

    def getstate(self):
        return self.state

    def getScore(self):
        return self.score

class assignScore(object):
    """Does the sentimental analysis for each tweet and gives it a score"""
    def __init__(self):
        self.scores = {}
        self.newDict = {}

    def getScore(self, term):
        try:
            return self.scores[term]
        except KeyError:
            return 0 

    def sentFile(self, sent_file):
        afinnfile = open(sent_file)
        for line in afinnfile:
            # print line
            term, score  = line.split("\t")  # The file is tab-delimited. 
            self.scores[term] = int(score)  # Convert the score to an integer.

    def calcTweetScore(self, sent_file, data):
        '''sets the sentiment score of every tweet'''
        self.sentFile(sent_file)
        words = []
        for i in xrange(len(data)): 
            twScore = 0.0
            tweet = data[i].getTweet()
            sentences = tweet.splitlines()
            for sentence in sentences: #iterate through each sentence in every tweet
                words = sentence.split(" ")
            for term in words:# iterate through each word in the tweet sentence
                twScore += self.getScore(term)
            data[i].setScore(twScore)
        
class readTweet(object):
    '''Reads the file with Twitter data into Python data structures (dict here) using the json module. 
    Extracts the tweet text and the associated location data called "state" into the objects of Tweet class'''
    def __init__(self):
        self.data = []

    def readData(self, tweet_file):
        TweetFile = open(tweet_file)
        totalTweets = 0.0
        for line in TweetFile:
            try:
                pyResponse = json.loads(line)
                place = pyResponse['place']
                nation = place['country_code']
                language = pyResponse['lang']
                # print language
                if nation == 'IN' and language=='en':
                    city = pyResponse['place']['full_name']
                    tweet = pyResponse['text'].encode('utf-8')
                    loc = city.split(", ")[0]
                    state = city.split(", ")[1]
                    twt = Tweet()
                    twt.setTweet(tweet)
                    twt.setState(state)
                    self.data.append(twt)
                    # self.data.extend(temp)
                    totalTweets += 1.0
            except:
                pass
                # print 'Some error '
        print totalTweets        
        return self.data

class calcAndPrintStats(object):
    def printStats(self):
        for key in happyStates.keys(): # finds the maximum happiness in a state
            if happyStates[key].count > 25:
                print key, "\t", (happyStates[key].score)/(happyStates[key].count), "\t", happyStates[key].count

def main():
    sent_file = str(sys.argv[1])
    tweet_file = str(sys.argv[2])
    tw = readTweet()
    tw.readData(tweet_file)
    ts = assignScore()
    ts.calcTweetScore(sent_file, tw.data)
    
    hs = happyState()
    hs.stateSort(tw.data)

    ps = calcAndPrintStats()    
    ps.printStats()

if __name__ == '__main__':
    if len(sys.argv)==3:
        main()
    else:
        print 'Please enter sentiment file and then tweet file in the format:'
        print '$python <python filename> <sentiment_file> <tweet_file>'        