import pyautogui
from PIL import ImageGrab
from pynput.mouse import Listener, Button

pixels = []
APos = (0, 0)
pixelColor = (255, 255, 255)
pixelColorPos = (0, 0)

config = input('Que voulez vous configurer ? a / color / pixels : ')


def on_click(x, y, button, pressed):
    if not pressed:
        return
    if button == Button.right:
        listener.stop()
        return

    pos = (x, y)
    print(pos)
    if config == 'a':
        APos = pos
        save(pos, 'APos.txt')
        listener.stop()
    elif config == 'color':
        pixelColor = checkColor(x, y)
        print(pixelColor)
        save( pixelColor, 'pixelColor.txt')
        save( pos, 'colorPos.txt')
        listener.stop()
    else:
        pixels.append(pos)
        print(pixels)
        save(pixels, 'pixels.txt')
        print('POUR STOP => CLIQUE DROIT')


def checkColor(x, y):
    return pyautogui.pixel(x, y)



def save(pixel, name):
    f = open(name, "w")
    f.write(str(pixel))
    f.close()


with Listener(on_click=on_click) as listener:
    listener.join()
