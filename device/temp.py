import paho.mqtt.client as mqtt # https://pypi.org/project/paho-mqtt/

import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("hola")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+": "+msg.payload.decode('utf-8'))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("group-c","92rj26cjPEpikY13")

client.connect("group-c.cloud.shiftr.io", 1883, 60)

# Si quiero que este escuchando para siempre:
# client.loop_forever()
# http://www.steves-internet-guide.com/loop-python-mqtt-client/

# Inicia una nueva hebra
client.loop_start()

while 1:
    # Publish a message every second
    client.publish("Topic", "Message", 1)
    time.sleep(1)

# También se puede conectar y enviar en una linea https://www.eclipse.org/paho/clients/python/docs/#single

# Y conectar y bloquear para leer una sola vez en una sola linea https://www.eclipse.org/paho/clients/python/docs/#simple