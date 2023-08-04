import datetime
import random
import time

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


def buy_bread():
    time.sleep(1)

    return random.choice(breads)


def slice_bread(bread):
    time.sleep(0.5)

    return 'sliced' + bread


def buy_cheese():
    time.sleep(1.5)

    return random.choice(cheeses)


def slice_cheese(cheese):
    time.sleep(3.5)

    return 'sliced' + cheese


def make_sandwich(sliced_cheese, sliced_bread):
    time.sleep(1.5)
    return sliced_cheese + ' ' + sliced_bread


def run_sync():
    bread = buy_bread()
    sliced_bread = slice_bread(bread)

    cheese = buy_cheese()
    sliced_cheese = slice_cheese(cheese)

    sandwich = make_sandwich(sliced_cheese, sliced_bread)

    print(sandwich)


def run():
    start = datetime.datetime.now()
    run_sync()
    end = datetime.datetime.now()

    print(f'Sandwich is ready in {end - start} seconds')


run()
