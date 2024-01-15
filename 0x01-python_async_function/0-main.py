#!/usr/bin/env python3

import asyncio
from 0-basic_async_syntax.py import wait_random

async def main():
    print(await wait_random())
    print(await wait_random(5))
    print(await wait_random(15))

# Create an event loop
loop = asyncio.get_event_loop()

# Run the main coroutine
loop.run_until_complete(main())
