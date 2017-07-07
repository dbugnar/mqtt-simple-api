import json


class Message(object):
    def __init__(self, topic, message, qos, time):
        self.topic = topic
        self.message = message
        self.qos = qos
        self.time = time

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
