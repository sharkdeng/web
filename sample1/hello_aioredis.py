#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 19:11:54 2019

@author: dph
"""


# Reference: https://aioredis.readthedocs.io/en/v1.3.0/start.html#installation

import asyncio
import aioredis


async def main():
    redis = await aioredis.create_redis_pool('redis://localhost')
    await redis.set('my-key', 'value')
    value = await redis.get('my-key', encoding='utf-8')
    print(value)

    redis.close()
    await redis.wait_closed()

asyncio.run(main())


# asyncio.run() cannot be called from a running event loop
# cannot run on jupyter, which is already a running event