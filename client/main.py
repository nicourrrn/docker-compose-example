import time

import requests

while True:
    requests.get('http://server')
    time.sleep(10)
