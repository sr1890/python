import tweepy
import time

auth = tweepy.OAuthHandler('tbn6gCiB98jS3MdTJX4Nplv2R', '4NTLCjOKNMc4QMEScLjIYTtjEIYVENtYDW4pcACEVhapdQ5z24')
auth.set_access_token('235907087-LnklhQrmRrN2dQP7IOefrJG4fCdNiEEUl2KyLOnx', '78qw2NBAyqH4Gg1uJfEne9tRjCRdsCB9ZvlDDPMINe71u')

api = tweepy.API(auth)
user = api.me()

# print("User details:")
# print(user.name)
# print(user.description)
# print(user.location)

# print("Last 20 Followers:")
# for follower in user.followers():
#     print(follower.name)


try: 
	api.verify_credentials ()
	print("Authentication Ok")
except:
    print("Error during authentication")


def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

# for follower in limit_handled(tweepy.Cursor(api.followers).items()):
#     if follower.friends_count < 300:
#         print (follower.screen_name)


search_string = 'RELIANCE'
numberOfTweets = 2

# Be a narcisist and love your own tweets. or retweet anything with a keyword!
for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)	


# timeline = api.home_timeline()
# for tweet in timeline:
#     print(f"{tweet.user.name} said {tweet.text}")


