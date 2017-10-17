from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient

access_token = "access_token"
access_token_secret = "access_token_secret"
consumer_key = "consumer_key"
consumer_secret = "consumer_secret"

class StdOutListener(StreamListener):
    def __init__(self):
        self.msg_count = 0

    def on_data(self, data):
        producer.send_messages("trump", data.encode('utf-8'))
        self.msg_count = self.msg_count + 1
        if self.msg_count % 20 == 0:
        print (data)
        return True
    def on_error(self, status):
        print (status)

kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=['trump'])


