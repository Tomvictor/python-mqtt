import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

#client = mqtt.Client()
#client.connect("technoripio.cloudapp.net", 8883, 60)
#print(client)
#client.publish("tracker", "temperature")

publish.single("tracker", payload="tom",hostname="technoripio.cloudapp.net",port=8883)
