import os
from flask import Flask, render_template
from flask_socketio import SocketIO
from argparse import ArgumentParser
import paho.mqtt.client as mqtt

parser = ArgumentParser()
parser.add_argument("-t", "--topics", dest="topics", nargs="+", required=True,
                    help="the topics that you want to subscribe to")
args = parser.parse_args()

app = Flask(__name__)
socketio = SocketIO(app)

subscribed_topics = []  # Lista para almacenar los temas suscritos


def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")


def config_Platform(client):
    print("Subscribing to main topics")
    for topic in args.topics:
        t = topic
        if topic.lower() == "all":
            t = "*"
        client.subscribe(f"security/{t}/*")
        client.subscribe(f"{t}/*")
        client.subscribe(f"{t}/")
        client.subscribe(f"{t}")
        subscribed_topics.append(f"security/{t}/*")  # Agregar a la lista de temas suscritos
    client.subscribe("newDevice/*")

    subscribed_topics.append("newDevice/*")  # Agregar a la lista de temas suscritos
    # Establecer el manejador de mensajes
    client.on_message = on_message


def connect_broker(client, userdata, flags, rc):
    if rc == 0:
        print("Running on http://localhost:5000")
        print('Connected successfully')
        config_Platform(client)
    else:
        print('Bad connection. Code:', rc)


if __name__ == '__main__':
    host = os.getenv("MQTT_BROKER_URL")
    port = 1883
    username = os.getenv("MQTT_USERNAME")
    password = os.getenv("MQTT_PASSWORD")
    client = mqtt.Client(client_id="Platform")
    client.username_pw_set("micalancer669", "tjeSCoiINVm89VAI")
    client.on_connect = connect_broker
    client.connect("micalancer669.cloud.shiftr.io", port, 60)
    client.loop_start()
    socketio.run(app, host='localhost', port=5000)
