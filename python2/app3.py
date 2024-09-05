from mqtt_ipc import MQTTIPCApp
import time
import random
import json

class App3(MQTTIPCApp):
    def __init__(self):
        super().__init__("App3")
        self.data["value"] = 0

    def custom_action(self):
        while True:
            print(f"App3 current value: {self.data['value']}")
            # 随机改变值
            self.data["value"] += random.randint(-5, 5)
            # 确保值在0-100之间
            self.data["value"] = max(0, min(100, self.data["value"]))
            # 发送通知
            self.client.publish(f"{self.app_name}/notify", json.dumps({"value": self.data["value"]}))
            time.sleep(3)

if __name__ == "__main__":
    app = App3()
    app.run()