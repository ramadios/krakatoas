import tweepy
auth = tweepy.OAuthHandler("VDKGw405vPiZTTIPcAG9x6F5t", "1MsOVxQpBNk5CFUNqNNc8L1kzJ8W21x8VgxQxydwtTxdZATsUe")
auth.set_access_token("1418700106849730560-o1vRbwBXa03pQPDOOx3yBxWemKtQLI", "O9moaU4ZP5fbMIn78pKCByYuMKi1JL4sfrd795cdftE9G")
api = tweepy.API(auth)
tweet = input("Hola")
api.update_status(status =(tweet))
print ("Done!")
