"""
    asyncio is a single-threaded, single process design. It uses "coperative multitasking"
    Asynchronous routines are routines that can be paused while waiting on their ultimate result, and let other routines run in the meantime.
    Asunchronous code, gives the look and feel of concurrency.
    It is used to provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.
    
    # https://realpython.com/async-io-python/
    The syntax async def introduces either a native coroutine or an asynchronous generator
    
    The keyword await passes function control back to the event loop. (It suspends the execution of the surrounding coroutine.) 
    If Python encounters an await f() expression in the scope of g(), this is how await tells the event loop, 
    “Suspend execution of g() until whatever I’m waiting on—the result of f()—is returned. In the meantime, go let something else run.”
    
    A function that you introduce with async def is a coroutine. It may use await, return, or yield, but all of these are optional.
    You can only use await in the body of coroutines.
    
    When you use await f(), it’s required that f() be an object that is awaitable. 
    awaitable object is either (1) another coroutine or (2) an object defining an .__await__() dunder method that returns an iterator
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
