import os
import threading
from argparse import ArgumentParser

import paho.mqtt.client as mqtt

from flask_socketio import SocketIO
from flask import app
from flask.cli import load_dotenv

parser = ArgumentParser()
parser.add_argument("-t", "--topics", dest="topics", nargs="+",
                    required=True, help="the topics that you want to subscribe to")


args = parser.parse_args()

load_dotenv()
socketio = SocketIO(app)
def config_Platform():
    print("Subscribing to main topics")
    for topic in args.topics:
            t = topic
            if topic.lower() == "all":
                t = "*"
            client.subscribe(f"security/{t}/*")
    client.subscribe("newDevice/*")

def connect_brocker(client, userdata, flags, rc):
    if rc == 0:
        print("Running on http://localhost:5000")
        print('Connected successfully')
        config_Platform()
    else:
        print('Bad connection. Code:', rc)

if __name__ == '__main__':
    host = os.getenv("MQTT_BROKER_URL")
    port = 1883
    username = os.getenv("MQTT_USERNAME")
    password = os.getenv("MQTT_PASSWORD")
    client = mqtt.Client(client_id="Platform")
    client.username_pw_set(username, password)
    client.on_connect = connect_brocker
    client.connect(host, port, 60)
    client.on_message = config_Platform
    client.loop_start()
    socketio.run(app, host='localhost', port=5000)
