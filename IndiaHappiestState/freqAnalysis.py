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
