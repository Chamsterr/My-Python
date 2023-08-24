import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed
from chapter_04 import fetch_status

async def main():
    async with ClientSession() as session:
        tasks = [fetch_status(session, 'https://www.example.com', x) for x in range(3)]
        
        for finished_task in asyncio.as_completed(tasks):
            print(await finished_task)

asyncio.run(main())