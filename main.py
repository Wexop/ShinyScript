import time
from datetime import datetime

import keyboard
import pyautogui
from PIL import ImageGrab
import ctypes

# startX = 546
# startY = 316

# buttonRpos = (979, 1167)
# buttonLpos = (159, 1140)
# buttonStartpos = (503, 1131)
# buttonSelectpos = (659, 1122)
# buttonAPos = (973, 2123)

f = open("pixels.txt", "r")
pixelCoords = eval(f.read())
f.close()
print(pixelCoords, "COORDS")

f = open("pixelColor.txt", "r")
pixelColor = eval(f.read())
f.close()
print(pixelColor, "COLOR")

f = open("colorPos.txt", "r")
colorPos = eval(f.read())
f.close()
print(colorPos, "COLOR POS")

f = open("APos.txt", "r")
APos = eval(f.read())
f.close()
print(APos, "APOS")

f = open("count.txt", "r")
count = eval(f.read())
f.close()
print(count, "COUNT")


# client = AdbClient(host="127.0.0.1", port=5037)
# device = client.device("192.168.1.164:5555")


def pressButton(pos, duration=0):
    # device.shell(f"input tap {pos[0]} {pos[1]}")
    pyautogui.click(pos[0], pos[1], duration=duration)


def checkColor(x, y):
    return pyautogui.pixel(x, y)


def onFound():
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, 'SHINY ????', 'Window title', 0)


def checkCloseColor(color1, color2):
    isClose = False
    avg2 = (color2[0] + color2[1] + color2[2]) / 3
    avg1 = (color1[0] + color1[1] + color1[2]) / 3

    if color1 == color2 or avg2 - 5 <= avg1 <= avg2 + 5:
        isClose = True

    return isClose


def checkCloseColor2(pos, color):
    return pyautogui.pixelMatchesColor(pos[0], pos[1], color, 5)


def saveFile(fileName, value):
    f = open(fileName, 'w')
    f.write(str(value))
    f.close()


find = False
lastTime = datetime.now()

pressButton(APos, 0.1)

while not find:
    print('NOMBRE ESSAIS : ', count)
    if keyboard.is_pressed('q'):
        break
    print('STARTED')
    # pressButton(APos, 0.1)
    pyautogui.keyDown('x')
    pyautogui.keyUp('x')

    if (datetime.now() - lastTime).seconds > 20:
        print('FOUND')
        find = True
        # onFound()

    print('COLOR CHECKED ', checkColor(colorPos[0], colorPos[1]), 'INITIAL COLOR ', pixelColor)
    print('POUR SORTIR DE LA BOUCLE : q')
    if checkCloseColor2(colorPos, pixelColor):
        count += 1
        saveFile('count.txt', count)
        for i in range(len(pixelCoords)):
            if keyboard.is_pressed('q'):
                break
            pressButton(pixelCoords[i])
        lastTime = datetime.now()
        delay = datetime.now()
        print('RERUN')
