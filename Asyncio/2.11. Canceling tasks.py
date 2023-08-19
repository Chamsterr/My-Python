import asyncio
from util import delay

async def canceling_long_process():
    for _ in range(2):
        print(f"{_}c")
        await asyncio.sleep(1)
    return False

async def main():
    downloading_task = asyncio.create_task(delay(6))

    result = await canceling_long_process()

    if not result:
        downloading_task.cancel()

    await downloading_task


asyncio.run(main())