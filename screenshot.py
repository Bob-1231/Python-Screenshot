import pyscreenshot as ImageGrab
import pynput
import os

num = 1

dir_name = 'images'
if not os.path.exists(dir_name):
    os.mkdir('./' + dir_name)

def on_press(key):
    global num
    if key == pynput.keyboard.KeyCode(char = 'e'):
        img = ImageGrab.grab(bbox = None)    # x1, y1, x2, y2, (None = Full Screen)
        img.save('./' + dir_name + '/' + str(num) + '.jpg')
        num += 1

def on_release(key):
    pass

listener = pynput.keyboard.Listener(
    on_press = on_press,
    on_release = on_release)
listener.start()

while True:
    pass

