import time
import os

def clear():
    os.system("clear")

def sleep(num):
    time.sleep(num)

def loading_animation(times_repeated):
    acum = 0
    while True:
        print("Loading")
        sleep(0.2)
        clear()
        print("Loading.")
        sleep(0.2)
        clear()
        print("Loading..")
        sleep(0.2)
        clear()
        print("Loading...")
        sleep(0.2)
        clear()
        acum += 1
        if acum == times_repeated:
            break


def custom_loading_animation(text_for_loading, times_repeated):
    x = 0
    while True:
        print(f"{text_for_loading}")
        sleep(0.2)
        clear()
        print(f"{text_for_loading}.")
        sleep(0.2)
        clear()
        print(f"{text_for_loading}..")
        sleep(0.2)
        clear()
        print(f"{text_for_loading}...")
        sleep(0.2)
        clear()
        x += 1
        if x == times_repeated:
            break
