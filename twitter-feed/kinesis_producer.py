from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import boto3

access_token = "access_token_here"
access_token_secret = "access_token_secret_here"
consumer_key = "consumer_key_here"
consumer_secret = "consumer_secret_here"

# Kinesis delivery stream name
delivery_stream = "Add delivery stream name"

record_list = []

class StdOutListener(StreamListener):
    def __init__(self):
        self.msg_count = 0

    def on_data(self, data):
        record_list.append({'Data': data.encode('utf-8')})
        self.msg_count = self.msg_count + 1
        if self.msg_count % 20 == 0:
            response = client.put_record_batch(DeliveryStreamName=delivery_stream, Records=record_list)
            record_list[:] = []
            print (data)
        return True
    def on_error(self, status):
        print (status)

client = boto3.client('firehose')

l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=['trump'])