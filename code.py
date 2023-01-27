import usb_hid
import board
import digitalio
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
keyList = []
currentKey = 0
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = False
#Button Setup
button = digitalio.DigitalInOut(board.BUTTON)
button.switch_to_input(pull=digitalio.Pull.UP)
downLow = digitalio.DigitalInOut(board.A2)
downLow.direction = digitalio.Direction.OUTPUT
downLow.value = True
upButton = digitalio.DigitalInOut(board.D12)
upButton.switch_to_input(pull=digitalio.Pull.DOWN)
downButton = digitalio.DigitalInOut(board.A4)
downButton.switch_to_input(pull=digitalio.Pull.DOWN)
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

#read the keyfile into a list
keyFile = open("/keys.txt", "r")
keyList = keyFile.readlines()
keyFile.close()
print("read", len(keyList), "keys")

while True:
    time.sleep(0.1)  # debounce delay
    if not button.value:
        led.value = True
        layout.write(keyList[currentKey].rstrip())
        led.value = False
        time.sleep(0.05)  # debounce delay
        while not button.value:
            pass
    if downButton.value and not upButton.value:
        currentKey += 1
        if currentKey > len(keyList) - 1:
            currentKey = 0
        print(keyList[currentKey])
        time.sleep(0.1)  # debounce delay
        while downButton.value:
            pass
    if upButton.value and not downButton.value:
        currentKey -= 1
        if currentKey < 0:
            currentKey = len(keyList) - 1
        print(keyList[currentKey])
        text_area.text = keyList[currentKey]
        while upButton.value:
            pass
