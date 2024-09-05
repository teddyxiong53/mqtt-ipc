from mqtt_ipc import MQTTIPCApp
import time

class App2(MQTTIPCApp):
    def __init__(self):
        super().__init__("App2")

    def custom_action(self):
        while True:
            self.get_value("App1", ["value"])
            time.sleep(2)
            self.set_value("App1", value=42)
            time.sleep(2)
            self.get_value("App3", ["value"])
            time.sleep(2)
            self.set_value("App3", value=99)
            time.sleep(2)

if __name__ == "__main__":
    app = App2()
    app.run()