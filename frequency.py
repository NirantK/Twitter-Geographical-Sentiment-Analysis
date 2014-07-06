import sys, json, codecs
 
def readData(tweet_file):
    oFile = open(tweet_file)
    newDict = {}
    Dict = {}
    total = 0.0
    for line in oFile:
        pyResponse = json.loads(line)
        try:
            pyResponse["delete"]
        except:
            result = pyResponse
            # print pyResponse.keys()        
            tweet =  result['text'].encode('utf-8')            
            sentences = tweet.splitlines()
            words = []
            # print sentences
            for sentence in sentences:
                words.extend(sentence.split(" "))
                # word.extend(words)
            # print word
            count = len(words)
            total += count
            for word in words:
                try:
                    newDict[word] += 1
                except:
                    newDict[word] = 1
    for key in newDict.keys():
        Dict[key] = newDict[key]/total
    #     # if(key.encode('utf-8')==''.encode('utf-8')):
    #         # print "rajath",Dict[key]
        if key!='':
           print key, Dict[key]
    # print newDict.keys()
def main():
    # sent_file = str(sys.argv[1])
    tweet_file = str(sys.argv[1])
  
    # var = scoreCounter()
    # var.readFile(sent_file)

    readData(tweet_file)    

if __name__ == '__main__':
    
    main()