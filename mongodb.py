from pymongo import MongoClient
from message import Message
import json
import os


data_base = os.getenv('DB')
if data_base is None:
    print('Data base not found as a environment variable')
    exit(1)
client = MongoClient(data_base)

db = client['mqtt-database']


def db_get_broker_info():
    collection = db['broker']
    document = collection.find_one({})
    return document


def db_get_topics():
    topics = []
    collection=db['topics']
    cursor = collection.find({})
    for document in cursor:
        for topic in document['topics']:
            topics.append(topic)
    return topics


def db_remove_topic(topic):
    collection = db['topics']
    document = collection.find_one()
    id_var = {}
    id_var['_id'] = document['_id']
    topics = document['topics']
    try:
        topics.remove(topic)
    except ValueError:
        return None
    collection.update(id_var, {'topics': topics})
    return topics


def db_get_all_messages():
    messages = []
    collection = db['messages']
    document = collection.find_one({})
    for topic in document:
        if '_id' != topic:
            for x in document[topic]:
                msg = Message(topic, x['message'], x['qos'], x['time'])
                messages.append(json.loads(msg.to_json()))
    return messages


def get_all_starting_form_time_messages(time):
    messages = []
    collection = db['messages']
    document = collection.find_one({})
    for topic in document:
        if '_id' != topic:
            for x in document[topic]:
                if x['time'] > time:
                    msg = Message(topic, x['message'], x['qos'], x['time'])
                    messages.append(json.loads(msg.to_json()))
    return messages


def get_messages_from_topic(topic):
    messages = []
    collection = db['messages']
    document = collection.find_one({})
    try:
        for x in document[topic]:
            msg = Message(topic, x['message'], x['qos'], x['time'])
            messages.append(json.loads(msg.to_json()))
    except (ValueError, KeyError):
        return []
    return messages


def get_messages_from_topic_stating_from_time(topic, time):
    messages = []
    collection = db['messages']
    document = collection.find_one({})
    try:
        for x in document[topic]:
            if x['time'] > time:
                msg = Message(topic, x['message'], x['qos'], x['time'])
                messages.append(json.loads(msg.to_json()))
    except ValueError:
        return []
    return messages
