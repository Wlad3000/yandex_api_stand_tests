import configuration
import requests
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.header_content)


def get_order(parameters):
    return requests.get(configuration.URL_SERVICE + configuration.REQUEST_ORDER,
                        params=parameters)