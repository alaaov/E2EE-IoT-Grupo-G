from random import random

import paho.mqtt.client as mqtt
import time


# Callback para cuando el cliente se conecta al servidor MQTT
def on_connect(client, userdata, flags, rc):
    print("Conectado con código de resultado: " + str(rc))

    # Suscribirse al tema "hola" al conectarse
    client.subscribe("hola")


# Callback para cuando se recibe un mensaje en un tema suscrito
def on_message(client, userdata, msg):
    print("Mensaje recibido en el tema " + msg.topic + ": " + msg.payload.decode('utf-8'))


# Configurar el cliente MQTT
client = mqtt.Client()

# Asignar los callbacks
client.on_connect = on_connect
client.on_message = on_message

# Establecer el nombre de usuario y contraseña si es necesario
client.username_pw_set("micalancer669", "tjeSCoiINVm89VAI")

# Conectar al servidor MQTT
client.connect("micalancer669.cloud.shiftr.io", 1883, 60)

# Iniciar un bucle en segundo plano para manejar la comunicación con el servidor MQTT
client.loop_start()

# Bucle principal para publicar mensajes y dormir durante un segundo
while True:
    # Publicar un mensaje en el tema "Topic"
    client.publish("temperatura", random()*100)
    # Esperar un segundo antes de publicar el siguiente mensaje
    time.sleep(1)
