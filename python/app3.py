import paho.mqtt.client as mqtt
import json
import time

class App3:
    def __init__(self):
        self.client = mqtt.Client("App3")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect("10.28.9.78", 1883, 60)
        self.data = {"value": 0}

    def on_connect(self, client, userdata, flags, rc):
        print("App3 connected with result code "+str(rc))
        self.client.subscribe("app3/get")
        self.client.subscribe("app3/set")
        self.client.subscribe("app1/notify")
        self.client.subscribe("app2/notify")

    def on_message(self, client, userdata, msg):
        topic = msg.topic
        payload = json.loads(msg.payload.decode())
        
        if topic == "app3/get":
            response = {"value": self.data["value"]}
            self.client.publish(f"app3/response/{payload['id']}", json.dumps(response))
        elif topic == "app3/set":
            self.data["value"] = payload["value"]
            print(f"App3: Value set to {self.data['value']}")
            self.client.publish("app3/notify", json.dumps({"value": self.data["value"]}))
        elif "notify" in topic:
            print(f"App3 received notification from {topic}: {payload}")

    def run(self):
        self.client.loop_start()
        while True:
            time.sleep(1)

if __name__ == "__main__":
    app = App3()
    app.run()