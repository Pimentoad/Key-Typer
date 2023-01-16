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
button = digitalio.DigitalInOut(board.BUTTON)
button.switch_to_input(pull=digitalio.Pull.UP)
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

#read the keyfile into a list
keyFile = open("/keys.txt", "r")
keyList = keyFile.readlines()
keyFile.close()
print("read", len(keyList), "keys")

while True:
    if not button.value:
        led.value = True
        layout.write(keyList[currentKey].rstrip())
        led.value = False
        while not button.value:
            pass