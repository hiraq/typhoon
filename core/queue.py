from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue, QueueEmpty

class TQueue(object):

    def __init__(self, maxsize=0, pause=0):

        self._queue = Queue(maxsize=maxsize)
        self._pause = pause
        self._items = list()

    def register_callback(self, callback):
        self._callback = callback

    def put(self, item):
        self._items.append(item)

    def is_item_exists(self):
        return True if len(self._items) > 0 else False

    @gen.coroutine
    def listen(self):

        while True:

            item = yield self._queue.get()

            try:

                yield gen.sleep(self._pause)
                yield self._callback(item)

            finally:

                self._queue.task_done()

    @gen.coroutine
    def _broadcast(self):
        for item in self._items:
            yield self._queue.put(item)

    @gen.coroutine
    def run(self):
        yield self._broadcast()
        IOLoop.current().spawn_callback(self.listen)
