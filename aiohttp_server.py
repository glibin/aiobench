import asyncio

from aiohttp import web


SLEEP_TIME = 0.05


async def handle(request):
    await asyncio.sleep(SLEEP_TIME)

    return web.json_response({'status': True})


def make_app():
    app = web.Application()

    app.router.add_route('GET', '/sleep', handle)

    return app


if __name__ == '__main__':
    web.run_app(make_app())
