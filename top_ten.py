import sys, json, collections

List = []
def readData(tweet_file):
    TweetFile = open(tweet_file)
    for line in TweetFile:
        pyResponse = json.loads(line)
        try:
            hashData = pyResponse['entities']['hashtags']
        except:
            pass
        try:
            hashtags = hashData[0]['text']
            List.append(hashtags)
        except:
            pass

    counter = collections.Counter(List)
    mostCommon = counter.most_common()
    for i in xrange(10):
        print mostCommon[i][0], mostCommon[i][1]


        
def main():
    tweet_file = str(sys.argv[1])
    readData(tweet_file)    

if __name__ == '__main__':
    
    main()