*TwitterSentimentAnalysis*
========================

Finds the Happiest US State based on Sentimental Analysis of Twitter Data

About **twitterstream.py**: Used to fetch live stream data from twitter. Requires oauth2, which is not part of the EnThought Python library. usage: Open the program and replace access_token_key, access_token_secret, consumer_key, and consumer_secret with the appropriate values. Then run $ python twitterstream.py 

To get credentials:
*Create a twitter account if you do not already have one.
*Go to https://dev.twitter.com/apps and log in with your twitter credentials.
*Click "create an application"
*Fill out the form and agree to the terms. Put in a dummy website if you don't have one you want to use.
*On the next page, scroll down and click "Create my access token"
*Copy your "Consumer key" and your "Consumer secret" into twitterstream.py
*Click "Create my access token." You can Read more about Oauth authorization.
*Open twitterstream.py and set the variables corresponding to the consumer key, consumer secret, access token, and access secret
*Run the following and make sure you see data flowing: $ python twitterstream.py

About **happiest_state.py**: Finds the happiest state in USA by doing a sentiment analysis of all the Tweets which have data about the 'place' in it. 