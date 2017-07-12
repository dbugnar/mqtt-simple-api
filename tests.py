from swagger_tester import swagger_test

# Dict containing the error you don't want to raise.
# By default, every status_code over other than 1xx, 2xx or 3xx
# will be considered as an error.
authorize_error = {
    'get': {
        '/broker/info': [200],
        '/messages/all': [200],
        '/messages/all/{time}': [200],
        '/messages/on_topic': [200],
        '/messages/on_topic/starting_from': [200],
        '/topics/list': [200]
    },
    'delete': {
        '/topics/remove/{topic}': [200],
        '/topics/remove/{topic}': [400]
    }
}


# Run the test with connexion
# An AssertionError will be raise in case of error.
swagger_test(app_url="http://localhost:12344", authorize_error=authorize_error)