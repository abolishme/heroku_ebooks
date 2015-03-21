'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'WHVMzJiXePy4iqnswGyYlx6Vl'
MY_CONSUMER_SECRET = 'Ie0dYNOABbFeT18xm44PdPAXLuCGwHkM1aj6Go4DEAuYgpmegY'
MY_ACCESS_TOKEN_KEY = '3102187408-VfmE7a4Q70bodBwiZ3Y1B56c1V2DB14kOE44gAV'
MY_ACCESS_TOKEN_SECRET = '9KK9pw4d08dyaZv7QHs39I46hq0tlGJ4qOsGKZUTwNws8'

SOURCE_ACCOUNTS = ["abolishme", "izzynastasia", "hannahurr"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 5 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "maskintern" #The name of the account you're tweeting to.
