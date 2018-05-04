import asyncio
import inspect
from functools import wraps

Future = asyncio.futures.Future
def coroutine(func):
	@wraps(func)
	def coro(*a, **k):
		res = func(*a, **k)
		if isinstance (res, Future) or inspect.isgenerator(res):
			res = yield from res
		return res
	return coro

@coroutine
def foo():
	yield from asyncio.sleep(1)
	print("HELLO FOO")

@asyncio.coroutine
def bar():
	print("Hello Bar")

loop = asyncio.get_event_loop()
tasks = [loop.create_task(foo()),loop.create_task(bar())]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()

