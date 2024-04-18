import math
import mouse
import time
from screeninfo import get_monitors
import random
from datetime import datetime
import os


center_x = 0
center_y = 0
radius = 50


def setup():
    print("CNTRL + C to exit")
    global center_x, center_y

    center_x = int(get_monitors()[0].width / 2)
    center_y = int(get_monitors()[0].height / 2)


def move_cursor():
    pos_x = 0
    pos_y = 0
    try:
        while True:
            for ang in range(0, 360):
                hour = datetime.now().strftime("%H")
                if int(hour) >= 19:
                    os.system("shutdown /s /t 1")
                pos_x = center_x + math.cos(math.radians(ang)) * radius
                pos_y = center_y + math.sin(math.radians(ang)) * radius
                mouse.move(pos_x, pos_y)
                if random.randint(1, 100) < 5:
                    mouse.click()
                time.sleep(0.005)

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    setup()
    move_cursor()
