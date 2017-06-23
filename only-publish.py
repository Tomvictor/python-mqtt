import paho.mqtt.publish as publish

publish.single("tracker", "payload", hostname="technoripio.cloudapp.net", port=8883)
