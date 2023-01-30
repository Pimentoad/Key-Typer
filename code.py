import usb_hid
import board
import digitalio
import time
import terminalio
from adafruit_display_text import bitmap_label
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.mouse import Mouse
keyList = []
currentKey = 0
#Button Setup
button = digitalio.DigitalInOut(board.BUTTON)
button.switch_to_input(pull=digitalio.Pull.UP)
downLow = digitalio.DigitalInOut(board.A3)
downLow.direction = digitalio.Direction.OUTPUT
downLow.value = True
upLow = digitalio.DigitalInOut(board.D13)
upLow.direction = digitalio.Direction.OUTPUT
upLow.value = True
upButton = digitalio.DigitalInOut(board.D11)
upButton.switch_to_input(pull=digitalio.Pull.DOWN)
downButton = digitalio.DigitalInOut(board.A5)
downButton.switch_to_input(pull=digitalio.Pull.DOWN)
#HID setup
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
m = Mouse(usb_hid.devices)
mouseJiggle = False

#read the keyfile into a list
keyFile = open("/keys.txt", "r")
keyList = keyFile.readlines()
keyFile.close()
print("read", len(keyList), "keys")
#display stuff
text = "Read " + str(len(keyList)) + " keys"
scale = 3
text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale)
text_area.x = 10
text_area.y = 64
board.DISPLAY.show(text_area)

while True:
    time.sleep(0.1)  # debounce delay
    if not button.value:
        if currentKey < len(keyList):
            layout.write(keyList[currentKey].rstrip())
        else:
            mouseJiggle = not mouseJiggle
        time.sleep(0.05)  # debounce delay
        while not button.value:
            pass
    if downButton.value and not upButton.value:
        currentKey += 1
        if currentKey > len(keyList):
            currentKey = 0
        if currentKey < len(keyList):
            print(keyList[currentKey])
            text_area.text = keyList[currentKey]
        else:
            text_area.text = "Mouse Jiggle"
        time.sleep(0.1)  # debounce delay
        while downButton.value:
            pass
    if upButton.value and not downButton.value:
        currentKey -= 1
        if currentKey < 0:
            currentKey = len(keyList)
        if currentKey < len(keyList):
            print(keyList[currentKey])
            text_area.text = keyList[currentKey]
        else:
            text_area.text = "Mouse Jiggle"
        time.sleep(0.1)  # debounce delay
        while upButton.value:
            pass
    if text_area.text == "Mouse Jiggle":
        if mouseJiggle:
            text_area.color=0x00FF00
        else:
            text_area.color=0x880000
    else:
        text_area.color=0xFFFFFF
    if mouseJiggle:
        m.move(-4, 0, 0)
        m.move(4, 0, 0)
        m.move(0, -4, 0)
        m.move(0, 4, 0)