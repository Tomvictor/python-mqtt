import paho.mqtt.client as mqtt
import requests
import array

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    print("on connect function initiated")
    topic = "tom/test"
    print("subscribing to the topic : ", topic)
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)
    print("Subscribed ok")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("message recieved")
    print("Received message '" + str(msg.payload) + "' on topic '"
          + msg.topic + "' with QoS " + str(msg.qos))
    message = str(msg.payload)
    topic = str(msg.topic)
    url = "http://iot.buildfromzero.com/store?q=" + message +"&t="+topic
    print(url)
    #r = requests.get('https://iot.buildfromzero.com/store?q='+ msg.payload + '&t=' + msg.topic)
    requests.get(url)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("13.67.186.62", 8883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()