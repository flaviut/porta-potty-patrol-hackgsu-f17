from datetime import datetime
from queue import Queue
from threading import Thread

import requests


class HttpClientThread(Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.daemon = True
        self._request_queue = Queue()

    def put_event(self, event_type, toilet_id):
        self._request_queue.put({
            'action': event_type,
            'toilet': toilet_id,
            'timestamp': datetime.now().isoformat()
        })

    def run(self):
        while True:
            next_update = self._request_queue.get()
            requests.post('http://54.211.92.19:5000/store/',
                          next_update)
