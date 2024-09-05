import paho.mqtt.client as mqtt
import json
import uuid
import time
import threading

class MQTTIPCApp:
    def __init__(self, app_name, broker_address="10.28.9.78", broker_port=1883):
        self.app_name = app_name
        self.client = mqtt.Client(app_name)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.connect(broker_address, broker_port, 60)
        self.data = {}

    def _on_connect(self, client, userdata, flags, rc):
        print(f"{self.app_name} connected with result code {rc}")
        self.client.subscribe(f"{self.app_name}/get")
        self.client.subscribe(f"{self.app_name}/set")
        self.client.subscribe("+/notify")

    def _on_message(self, client, userdata, msg):
        topic = msg.topic
        payload = json.loads(msg.payload.decode())
        
        if topic == f"{self.app_name}/get":
            self._handle_get(payload)
        elif topic == f"{self.app_name}/set":
            self._handle_set(payload)
        elif "notify" in topic:
            self._handle_notify(topic, payload)

    def _handle_get(self, payload):
        response = {key: self.data.get(key) for key in payload.get("keys", [])}
        self.client.publish(f"{self.app_name}/response/{payload['id']}", json.dumps(response))

    def _handle_set(self, payload):
        for key, value in payload.items():
            if key != "id":
                self.data[key] = value
                print(f"{self.app_name}: {key} set to {value}")
        self.client.publish(f"{self.app_name}/notify", json.dumps(self.data))

    def _handle_notify(self, topic, payload):
        print(f"{self.app_name} received notification from {topic}: {payload}")

    def get_value(self, app, keys):
        request_id = str(uuid.uuid4())
        self.client.subscribe(f"{app}/response/{request_id}")
        self.client.publish(f"{app}/get", json.dumps({"id": request_id, "keys": keys}))

    def set_value(self, app, **kwargs):
        self.client.publish(f"{app}/set", json.dumps(kwargs))

    def run(self):
        self.client.loop_start()
        
        # 在新线程中运行custom_action
        custom_action_thread = threading.Thread(target=self.custom_action)
        custom_action_thread.daemon = True
        custom_action_thread.start()
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"{self.app_name} is shutting down...")
        finally:
            self.client.loop_stop()

    def custom_action(self):
        # 子类应该重写此方法以添加自定义行为
        pass