"""
    asyncio is a single-threaded, single process design. It uses "coperative multitasking"
    Asynchronous routines are routines that can be paused while waiting on their ultimate result, and let other routines run in the meantime.
    Asunchronous code, gives the look and feel of concurrency.
    It is used to provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.
"""

import asyncio


async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    start_time = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start_time
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
