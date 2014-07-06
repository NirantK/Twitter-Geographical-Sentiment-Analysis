import sys, json

happyState = {}
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

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

    def substitute(self, stateName):
        for key in states.keys():
            if states[key]==stateName:
                return key

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
                    print city
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
          
def stateSort(data):
    '''simply calculates the happiness for each state by iterating through the state dict and data from Twitter'''
    for key in states.keys():
        for i in xrange(len(data)):
            if data[i].getStateCode() == key:
                try:
                    happyState[key] += data[i].getScore()
                except:
                    happyState[key] = data[i].getScore()

def main():
    sent_file = str(sys.argv[1])
    tweet_file = str(sys.argv[2])
    tw = readTweet()
    tw.readData(tweet_file)
    # print type(tw.data)
    ts = tweetScore()
    ts.calcTweetScore(sent_file, tw.data)
    # for i in xrange(len(tw.data)):
    #     print tw.data[i].getStateCode(), tw.data[i].getScore(), tw.data[i].getTweet()
    
    # stateSort(tw.data)
    # maximum = -9999999999999
    # for key in happyState.keys(): # finds the maximum happiness in a state
    #     # print key, happyState[key]
    #     if happyState[key] > maximum: 
    #         maximum = happyState[key]

    # for key in happyState.keys():  #finds the happiest state
    #     if happyState[key]==maximum:
    #         print key

if __name__ == '__main__':
    main()