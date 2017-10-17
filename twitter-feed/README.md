# Twitter feed example

Examples modified from: https://github.com/heroku/kafka-message-waterfall and http://www.bmc.com/blogs/working-streaming-twitter-data-using-kafka/

Install kafka:
`brew install kafka`

Install pre-requisites:
```npm install
pip install kafka-python
pip install python-twitter
pip install tweepy```

Start kafka & zookeeper: 
`zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties & kafka-server-start /usr/local/etc/kafka/server.properties`

Add twitter authentication tokens to kafka-producer.py and start it using:
`python kafka-producer.py`

Set up environment variables
```export KAFKA_URL=localhost:9092
export KAFKA_TOPIC=trump```

Run node.js app
`node app.js`
