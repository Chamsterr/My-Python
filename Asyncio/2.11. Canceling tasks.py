import asyncio
from util import delay


#Моя попытка :)
# async def canceling_long_process():
#     for _ in range(2):
#         print(f"{_}c")
#         await asyncio.sleep(1)

#     return False

# async def main():
#     downloading_task = asyncio.create_task(delay(6))

#     result = await canceling_long_process()

#     if not result:
#         downloading_task.cancel()

#     await downloading_task


# asyncio.run(main())


from asyncio import CancelledError

async def main():
    long_task = asyncio.create_task(delay(10))

    second_elapsed = 0

    while not long_task.done():
        print("Задача не закончилась, сдед проверка через секунду.")
        await asyncio.sleep(1)
        second_elapsed = second_elapsed + 1
        if second_elapsed == 5:
            long_task.cancel()
    
    try:
        await long_task
    except CancelledError:
        print("Задача снята")


asyncio.run(main())