from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue, QueueEmpty

class TQueue(object):
    """Typhoon Queue Processor

    This class is a wrapper of Tornado's queue utility.
    Read more detail about Tornado's queue here:
    http://www.tornadoweb.org/en/stable/queues.html

    This class can be used as background job, it's process detached
    from current IOLoop process.

    Usage:

        q = TQueue()
        q.put('item_1')
        q.put('item_2')

        @gen.coroutine
        def listener(item):
            logger.debug(item)
            raise gen.Return(item)

        q.register_callback(listener)
        yield q.run()


    Attributes:
        _queue : An instance of Tornado's Queue class
        _pause : Time to pause current queue process
        _items : A list of item that need to be processing
        _callback : A consumer of queue items
    """

    def __init__(self, maxsize=0, pause=0):
        """Class construct

        Setup optional configurations for :
        - maxsize
        - pause

        And also initialize an empty new item list.

        Args:
            maxsize (optional) = Maximum item can be put in queue
            pause (optional) = A float or int indicate how loang queue pending their processes
        """
        self._queue = Queue(maxsize=maxsize)
        self._pause = pause
        self._items = list()

    def register_callback(self, callback):
        """Register Callback

        Register a callback function or method to continue process
        an item inside queue.

        Args:
            callback : A function or class method
        """
        self._callback = callback

    def put(self, item):
        """Put Item

        Put an item inside queue item list.

        Args:
            item : A value can be string ,integer or anything.
        """
        self._items.append(item)

    def is_item_exists(self):
        """Check Item List

        Check if list of items is empty or not.

        Returns:
            A boolean value indicate queue items is empty or not.
        """
        return True if len(self._items) > 0 else False

    @gen.coroutine
    def listen(self):
        """IOLoop Spawn Callback Listener

        Attach this method into self container spawn process
        and detached from current IOLoop main process.
        """
        while True:

            # get an item from queue if any
            item = yield self._queue.get()

            try:

                # pause the spawn process so can be run other time
                # detached from main process
                yield gen.sleep(self._pause)

                # call the callback function or method and give the item
                # to process
                yield self._callback(item)

                # TODO:
                # Should we register an event to indicate that current queue
                # state is empty or full ?
                # More detail: http://www.tornadoweb.org/en/stable/queues.html#exceptions

            finally:

                # after each item processed, it assumed that
                # task has been done
                self._queue.task_done()

    @gen.coroutine
    def _broadcast(self):
        """Broadcast Items

        This protected method used to process all item registered and put
        it into queue.
        """

        # TODO:
        # We need to make sure first if item list is empty or not
        # before begin to loop.
        for item in self._items:
            yield self._queue.put(item)

    @gen.coroutine
    def run(self):
        """Run Queue Processor

        Broadcast all items and start to detached queue process from IOLoop
        main process.
        """
        yield self._broadcast()
        IOLoop.current().spawn_callback(self.listen)
