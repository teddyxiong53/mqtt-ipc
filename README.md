# mqtt-ipc
使用mqtt来做ipc通信。

## python

各个应用直接，可以互相get/set，可以notify。

而且在get的时候，还临时订阅了一个消息，这个跟我之前的想法是一致的。

3个应用：

app1.py

app2.py

app3.py

3个shell窗口分别启动。

需要改一下mqtt broker的地址。我是在一台服务器上安装了mosquitto来做broker的。

```
python app1.py
App1 connected with result code 0
App1: Value set to 42
App1: Value set to 42
App1: Value set to 42
App1 received notification from app3/notify: {'value': 99}
App1: Value set to 42
```

```
python .\app2.py
App2 connected with result code 0
App2 received response: {'value': 0}
App2 received notification from app1/notify: {'value': 42}
App2 received response: {'value': 42}
App2 received notification from app1/notify: {'value': 42}
```



```
python app3.py
App3 connected with result code 0
App3 received notification from app1/notify: {'value': 42}
App3: Value set to 99
App3 received notification from app1/notify: {'value': 42}
App3: Value set to 99
App3 received notification from app1/notify: {'value': 42}
```

## python2

这个是对python目录下的代码进行一次抽象。



