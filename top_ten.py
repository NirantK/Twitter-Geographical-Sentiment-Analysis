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
    for key in counter.keys():
        print key.encode('utf-8'), counter[key]


        
def main():
    tweet_file = str(sys.argv[1])
    readData(tweet_file)    

if __name__ == '__main__':
    
    main()