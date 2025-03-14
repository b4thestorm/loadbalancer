from flask import Flask, request
import random
import yaml
import requests

loadbalancer = Flask(__name__)

def load_configuration(path):
    with open(path) as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)
    return config

config = load_configuration('loadbalancer.yaml')

########HOST BASED ROUTING
@loadbalancer.route('/')
def router():
    host_header = request.headers['Host']
    for entry in config['hosts']:
        if host_header == entry['host']:
            response = requests.get(f'http://{random.choice(entry["servers"])}')
            return response.content, response.status_code
    return 'Not Found', 404



#######PATH BASED ROUTING
@loadbalancer.route('/mango')
def mango_path():
    response = requests.get(f'http://{random.choice(MANGO_BACKENDS)}')
    return response.content, response.status_code

@loadbalancer.route('/apple')
def apple_path():
    response = requests.get(f'http://{random.choice(APPLE_BACKENDS)}')
    return response.content, response.status_code

