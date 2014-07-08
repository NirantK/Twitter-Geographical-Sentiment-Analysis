import sys, json, collections

'''Written with <3 by Nirant Kasliwal, Undergraduate Information Systems Student at BITS Pilani
Email: nirant[]bits[at]gmail[ dot]com'''

happyStates = {}

words_to_ignore = ["to","are","for","we","of", "@", "&amp",
 "on", "my", "at", "it", "our","they", "he", "so", 
 "the","in","a", "is", "and" ,"that","what","you","u","r",
 "with","this","would","from","your","which","hai", "", " "
 "while","these"]

wordsToNotice = ["rail","train","rail budget", "trains", "railway"]
things_to_strip = [".","http","t.co" ,"-",",","?",")","(","\"",":",";","'s"]

class happyState(object):
    def __init__(self):
        self.stateName = ""
        self.count = 0
        self.score = 0.0
        self.tweet = ""
        self.isRailBudget = False

    def setName(self, name):
        self.stateName = name

    def updateCount(self):
        self.count += 1.0

    def updateScore(self, newScore):
        self.score += newScore

def stateSort(data):
    for i in xrange(len(data)):
        key = data[i].getStateCode()
        try:
            happyStates[key] 
        except KeyError:
            happyStates[key] = happyState()
            happyStates[key].stateName = key
        finally:
            happyStates[key].score += data[i].getScore()
            happyStates[key].updateCount()
            happyStates[key].tweet += "\t" + data[i].getTweet()

class Tweet:
    '''Stores the necessary data for each tweet'''
    def __init__(self):
        self.tweet = ""
        self.stateCode = ""
        self.score = 0.0

    def setStateCode(self, stateCode):
        self.stateCode = stateCode

    def setTweet(self, tweet):
        self.tweet = tweet

    def setScore(self, score):
        self.score = score

    def getTweet(self):
        return self.tweet

    def getStateCode(self):
        return self.stateCode

    def getScore(self):
        return self.score

class tweetScore(object):
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
            term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
            self.scores[term] = int(score)  # Convert the score to an integer.

    def calcTweetScore(self, sent_file, data):
        self.sentFile(sent_file)
        words = []
        for i in xrange(len(data)):
            twScore = 0.0
            tweet = data[i].getTweet()
            sentences = tweet.splitlines()
            for sentence in sentences:
                words = sentence.split(" ")
                # print words
            for term in words:
                twScore += self.getScore(term)
            # print tweet, twScore
            data[i].setScore(twScore)
        
class readTweet(object):
    '''Reads the file with Twitter data into Python objects (dict here) using the json module. 
    Extracts the tweet text and the associated location data called "stateCode" into the objects of Tweet class'''
    def __init__(self):
        self.data = []

    # def substitute(self, stateName):
    #     for key in states.keys():
    #         if states[key]==stateName:
    #             return key

    def readData(self, tweet_file):
        TweetFile = open(tweet_file)
        for line in TweetFile:
            try:
                pyResponse = json.loads(line)
            except:
                pass
            try:
                place = pyResponse['place']
                nation = place['country_code']
                if nation == 'IN':
                    # print pyResponse['place']['full_name'],"***",pyResponse['text'].encode('utf-8')
                    city = pyResponse['place']['full_name']
                    tweet = pyResponse['text'].encode('utf-8')
                    loc = city.split(", ")[0]
                    stateCode = city.split(", ")[1]
                    # print city
                    # if stateCode =='USA':
                    #     stateCode = self.substitute(loc)
                    # print stateCode, tweet
                    twt = Tweet()
                    twt.setTweet(tweet)
                    twt.setStateCode(stateCode)
                    self.data.append(twt)
                    # self.data.extend(temp)
            except:
                pass
        return self.data

def freqAnalysis(key):
    # for key in happyStates.keys():
    words = []
    tempWords = []
    rawWords = happyStates[key].tweet.split(" ")
    # print rawWords[0]
    # x = False
    impTweets = 0.0
    for word in rawWords:
        for thing in things_to_strip:
            if thing in word:
                word = word.replace(thing,"")
        if word.lower() not in words_to_ignore:
            words.append(word)
            if word in wordsToNotice:
                happyStates[key].isRailBudget = True
                impTweets += 1
                # print happyStates[key].tweet

    # print words
    counter = collections.Counter(words)
    mostCommon = counter.most_common()
    z = len(mostCommon)/100
    j = 0.0 
    # for i in xrange(len(mostCommon)):
        # print mostCommon[i][0], mostCommon[i][1]
    #     ele = mostCommon[i][0].lower()
    #     if ele=='i' or ele=='me':
    #         print mostCommon[i]
    #         j += mostCommon[i][1]
    # print "Narcissist Value:",j/len(words)
    # print "Happiness Value:",(happyStates[key].score)/(happyStates[key].count)
    print impTweets
    # print
    # mostCommon = [x[0] for x in mostCommon]


def main():
    sent_file = str(sys.argv[1])
    tweet_file = str(sys.argv[2])
    tw = readTweet()
    tw.readData(tweet_file)
    # print type(tw.data)
    ts = tweetScore()
    ts.calcTweetScore(sent_file, tw.data)
    
    hs = happyState()
    stateSort(tw.data)
    total = 0.0 
    for key in happyStates.keys(): # finds the maximum happiness in a state
        if happyStates[key].count > 25:
            print key, "\t", (happyStates[key].score)/(happyStates[key].count), "\t", happyStates[key].count
    #         total += happyStates[key].count
    # print total
            freqAnalysis(key)
            # print key, happyStates[key].count
    #     if happyState[key] > maximum: 
    #         maximum = happyState[key]

    # for key in happyState.keys():  #finds the happiest state
    #     if happyState[key]==maximum:
    #         print key

if __name__ == '__main__':
    if len(sys.argv)==3:
        main()
    else:
        print 'Please enter sentiment file and then tweet file in the format:'
        print '$python happiest_state_India.py <sentiment_file> <tweet_file>'
        