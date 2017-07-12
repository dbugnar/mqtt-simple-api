#!/usr/bin/env python3

import connexion
from flask_cors import CORS
from flask import Response
from mongodb import *


def broker_info():
    broker = db_get_broker_info()
    del broker['_id']
    if broker_info == None:
        resp = {'status': 'Failed to get broker info.'}
        return Response(json.dumps(resp), status=400, mimetype='application/json')
    return Response(json.dumps(broker), status=200, mimetype='application/json')


def topics_list():
    topics = db_get_topics()
    if topics == None:
        resp = {'status': 'Failed to get topics list.'}
        return Response(json.dumps(resp), status=400, mimetype='application/json')
    return Response(json.dumps(topics), status=200, mimetype='application/json')


def remove_topic(topic):
    rt = db_remove_topic(topic)
    if rt ==  None:
        resp = {'message': 'Failed to remove topic list.', 'fields': 'Remove Topic'}
        return Response(json.dumps(resp), status=400, mimetype='application/json')
    resp = {'status': 'Topic removed successfully'}
    return Response(json.dumps(resp), status=200, mimetype='application/json')


def get_all_messages():
    messages = db_get_all_messages()
    print(messages)
    if messages ==  None:
        resp = {'status': 'Failed to get messages from topics list.'}
        return Response(json.dumps(resp), status=400, mimetype='application/json')
    return Response(json.dumps(messages), status=200, mimetype='application/json')


def get_topic_messages(topic):
    messages = get_messages_from_topic(topic)
    if messages == None:
        resp = {'status': 'Failed to get messages from topic list.'}
        return Response(json.dumps(resp), status=400, mimetype='application/json')
    return Response(json.dumps(messages), status=200, mimetype='application/json')


def get_all_messages_stating_from(time):
    messages = get_all_starting_form_time_messages(time)
    if messages ==  None:
        resp = {'status': 'Failed to get messages from topics list.'}
        return Response(json.dumps(resp), status=400, mimetype='application/json')
    return Response(json.dumps(messages), status=200, mimetype='application/json')


def get_topic_messages_starting_from(topic, time):
    messages = get_messages_from_topic_stating_from_time(topic, time)
    if messages ==  None:
        resp = {'status': 'Failed to get messages from topics list.'}
        return Response(json.dumps(resp), status=400, mimetype='application/json')
    return Response(json.dumps(messages), status=200, mimetype='application/json')



app = connexion.App(__name__, specification_dir='swagger/')
app.add_api('swagger.yaml')
cors = CORS(app.app)
application = app.app

if __name__ == '__main__':
    # run our standalone gevent server
    app.run(port=12344, server='gevent')


