var server = require('http').createServer();
var url = require('url');
var WebSocketServer = require('ws').Server;
var express = require('express');
var app = express();
var routes = require('./routes');

const Kafka = require('no-kafka');

const topic = process.env.KAFKA_TOPIC || 'test';

/*
 * Configure web app pieces
 *
 */
app.set('views', './views');
app.set('view engine', 'pug');
app.get('/', routes.index);
const port = process.env.PORT || 3000;
server.on('request', app);
server.listen(port, function() {
  console.log(`http/ws server listening on ${port}`);
});

/*
 * Configure WebSocketServer
 *
 */
var wss = new WebSocketServer({ server: server });
wss.on('connection', function connection(ws) {
  ws.on('open', function() {
    console.log('New WebSocket connection');
  });

  ws.on('close', function() {
    console.log('WebSocket connection closed');
  });
});

/*
 * Send messages received from Kafka consumer out over WebSocket
 *
 */
wss.broadcast = function broadcast(data) {
  wss.clients.forEach(function each(client) {
    client.send(data);
  });
};

const dataHandler = function (messageSet, topic, partition) {
  messageSet.forEach(function (m) {
    wss.broadcast(m.message.value.toString('utf8'));
  });
};

/*
 * Configure Kafka consumer
 *
 */
const brokerUrls = process.env.KAFKA_URL.replace(/\+ssl/g,'');
const consumer = new Kafka.SimpleConsumer({
  idleTimeout: 100,
  clientId: 'simple-consumer',
  connectionString: brokerUrls,
});

return consumer.init().then(function () {
  // Subscribe partiton 0 in a topic:
  return consumer.subscribe(topic, [0], dataHandler);
});
