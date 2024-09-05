import paho.mqtt.client as mqtt
import json
import time
import uuid

class App2:
    def __init__(self):
        self.client = mqtt.Client("App2")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect("10.28.9.78", 1883, 60)

    def on_connect(self, client, userdata, flags, rc):
        print("App2 connected with result code "+str(rc))
        self.client.subscribe("app2/response/+")
        self.client.subscribe("app1/notify")
        self.client.subscribe("app3/notify")

    def on_message(self, client, userdata, msg):
        topic = msg.topic
        payload = json.loads(msg.payload.decode())
        
        if "response" in topic:
            print(f"App2 received response: {payload}")
        elif "notify" in topic:
            print(f"App2 received notification from {topic}: {payload}")

    def get_value(self, app):
        request_id = str(uuid.uuid4())
        self.client.subscribe(f"{app}/response/{request_id}")
        self.client.publish(f"{app}/get", json.dumps({"id": request_id}))

    def set_value(self, app, value):
        self.client.publish(f"{app}/set", json.dumps({"value": value}))

    def run(self):
        self.client.loop_start()
        while True:
            self.get_value("app1")
            time.sleep(2)
            self.set_value("app1", 42)
            time.sleep(2)
            self.get_value("app3")
            time.sleep(2)
            self.set_value("app3", 99)
            time.sleep(2)

if __name__ == "__main__":
    app = App2()
    app.run()