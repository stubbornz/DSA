import pyautogui
from PIL import Image, ImageGrab
from time import sleep
# from numpy import asarray


def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    for i in range(1070, 1145):
        for j in range(300, 487):
            if data[i, j] > 250:
                return True
    return False

hit("up")
sleep(2)
while True:
    image = ImageGrab.grab().convert("L")
    data = image.load()
    # print(asarray(image))
    print(isCollide(data))
    if isCollide(data):
        hit("up")
    #
    # for i in range(1070, 1145):
    # for j in range(300, 487):
    #     data[i, j] = 0

#
# image = take_screenshot()
# data = image.load()
#     # print(asarray(image))
# if isCollide(data):
#     hit("up")
#
# for i in range(1070, 1145):
#     for j in range(300, 487):
#         data[i, j] = 0
#
# image.show()
#

