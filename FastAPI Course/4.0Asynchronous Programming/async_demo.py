import asyncio
from timeit import default_timer as timer



async def run_task(name,seconds):
    print(f'{name} started at {timer()}')
    await asyncio.sleep(seconds)
    print(f'{name} processsed at {timer()}')


async def main():
    start = timer()
    await asyncio.gather(
        run_task('Task 1',2),
        run_task('Task 2',1),
        run_task('Task 3',3)
    )
    print(f'Time taken to complete the task {timer()-start}')


asyncio.run(main())
