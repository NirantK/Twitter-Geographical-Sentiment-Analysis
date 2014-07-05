import sys, json
class scoreCounter:
    def __init__(self):
        self.scores = {}

    def readFile(self, sent_file):
        afinnfile = open(sent_file)
        for line in afinnfile:
            term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
            self.scores[term] = int(score)  # Convert the score to an integer.
        
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def getScore(var, term):
    # print var.scores
    try:
        return var.scores[term]
    except KeyError:
        return 0 
 
def readData(var, tweet_file, sent_file):
    oFile = open(tweet_file)
    newDict = {}
    for line in oFile:
        pyResponse = json.loads(line)
        try:
            pyResponse["delete"]
        except:
            result = pyResponse
            # print pyResponse.keys()
            tweet =  result['text'].encode('utf-8')
            score = 0
            words = tweet.split(" ")
            for word in words:
                score+=getScore(var, word)
            # print score
            for word in words:
                try:
                    newDict[word] = newDict[word]+score*0.1
                except:
                    newDict[word] = score*0.1
    for key in newDict:
        print key, newDict[key]

def main():
    sent_file = str(sys.argv[1])
    tweet_file = str(sys.argv[2])
  
    var = scoreCounter()
    var.readFile(sent_file)

    readData(var, tweet_file,sent_file)    

if __name__ == '__main__':
    
    main()