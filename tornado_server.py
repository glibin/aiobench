import asyncio

import tornado.ioloop
import tornado.web


SLEEP_TIME = 0.05


class SleepHandler(tornado.web.RequestHandler):
    def compute_etag(self):
        return None

    async def get(self):
        await asyncio.sleep(SLEEP_TIME)
        self.finish({'status': True})


def make_app():
    return tornado.web.Application([
        (r'/sleep', SleepHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
