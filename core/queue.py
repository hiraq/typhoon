from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue, QueueEmpty

class TQueue(object):

    def __init__(self, maxsize=0, pause=0):

        self._queue = Queue(maxsize=maxsize)
        self._pause = pause
        self._items = list()
        self._queue_empty = False

    def register_callback(self, callback):
        self._callback = callback

    def put(self, item):
        self._items.append(item)
        self._queue_empty = False

    def is_item_exists(self):
        return True if len(self._items) > 0 else False

    def is_queue_empty(self):
        return self._queue_empty

    @gen.coroutine
    def listen(self):

        while True:

            item = yield self._queue.get()

            try:

                yield gen.sleep(self._pause)
                yield self._callback(item)

            except QueueEmpty:
                self._queue_empty = True

            finally:

                self._queue.task_done()

    @gen.coroutine
    def _broadcast(self):
        for item in self._items:
            yield self._queue.put(item)

    def run(self):
        self._broadcast()
        IOLoop.current().spawn_callback(self.listen)
