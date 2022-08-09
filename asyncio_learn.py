import asyncio

async def foo(x: int):
    print(x)
    await asyncio.sleep(1)

l = []

async def main():
    for x in range(200):
        l.append(asyncio.create_task(foo(x)))

    asyncio.gather(*l)

eloop = asyncio.get_event_loop()
eloop.run_until_complete(main())
