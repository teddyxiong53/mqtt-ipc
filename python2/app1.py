from mqtt_ipc import MQTTIPCApp
import time

class App1(MQTTIPCApp):
    def __init__(self):
        super().__init__("App1")
        self.data["value"] = 0

    def custom_action(self):
        while True:
            print(f"App1 current value: {self.data['value']}")
            time.sleep(5)

if __name__ == "__main__":
    app = App1()
    app.run()