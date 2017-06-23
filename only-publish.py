import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("technoripio.cloudapp.net", 8883, 60)
client.publish("tracker", "temperature")
