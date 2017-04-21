# import threading
# import asyncio
# async def hello():
#     print('hello world(%s)' % threading.currentThread())
#     await asyncio.sleep(1)
#     print('hello thread2(%s)' % threading.currentThread())
# loop = asyncio.get_event_loop()
# tasks = [hello(),hello()]
# loop.run_until_complete(asyncio.wait(tasks))
#  loop.close()

'''async web application'''
from aiohttp import web
import asyncio
async def index(request):
    await asyncio.sleep(0.5)
    return web.Reponse(body=b'<h1>Index</h1>')
async def hello(request):
    await asyncio.sleep(0.5)
    text='<h1>hello,%s</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))
async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    app.router.add_route('GET','/hello/{name}', hello)
    srv=await loop.create_server(app.make_handler(),'127.0.0.1',9000)
    print('Server started at http://127.0.0.1:8000')
    return srv
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()