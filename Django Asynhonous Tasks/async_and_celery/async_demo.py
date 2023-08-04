import asyncio
import datetime
import random

breads = [
    'white',
    'banana',
    'multigrain'
]

cheeses = [
    'yellow cheese',
    'brie',
    'white cheese'
]


async def buy_bread():
    # time.sleep(1)
    await asyncio.sleep(1)
    return random.choice(breads)


async def slice_bread(bread):
    await asyncio.sleep(0.5)

    return 'sliced' + bread


async def buy_cheese():
    await asyncio.sleep(1.5)

    return random.choice(cheeses)


async def slice_cheese(cheese):
    await asyncio.sleep(3.5)

    return 'sliced' + cheese


async def make_sandwich(sliced_cheese, sliced_bread):
    await asyncio.sleep(1.5)
    return sliced_cheese + ' ' + sliced_bread


async def buy_and_slice_bread():
    bread = await buy_bread()
    sliced_bread = await slice_bread(bread)
    return sliced_bread


async def buy_and_slice_cheese():
    cheese = await buy_cheese()
    sliced_cheese = await slice_cheese(cheese)

    return sliced_cheese


async def run_async():
    (sliced_cheese, sliced_bread) = await asyncio.gather(
        buy_and_slice_cheese(),
        buy_and_slice_bread()
    )
    sandwich = await make_sandwich(sliced_cheese, sliced_bread)

    print(sandwich)


async def run():
    start = datetime.datetime.now()
    await run_async()
    end = datetime.datetime.now()

    print(f'Sandwich is ready in {end - start} seconds')


asyncio.run(run())
