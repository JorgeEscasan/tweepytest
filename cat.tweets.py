from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = '9aj4GEuESp7ZQUROeoSQFXfrH'
csecret = 'a0YWjZ0oHrz3NL2oY06R7HUnH0GeFXwEDurZq5EM352Qe3YOYS'
atoken = '2249860142-9HZBr6dvOlSq7tAV237DG949ShAdkzggQ2laUTo'
asecret = 'yntB2C592p5pW9tfaRtkQbKR9frdVM0t7xzQhhXJjxZyG'

class listener(StreamListener):

    def on_data(self, data):
        print len(data)
        return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["cat"])
