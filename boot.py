import board
import digitalio
import storage
import usb_cdc
import usb_hid
downLow = digitalio.DigitalInOut(board.A3)
downLow.direction = digitalio.Direction.OUTPUT
downLow.value = True
upLow = digitalio.DigitalInOut(board.D13)
upLow.direction = digitalio.Direction.OUTPUT
upLow.value = True
upButton = digitalio.DigitalInOut(board.D11)
upButton.switch_to_input(pull=digitalio.Pull.DOWN)
downButton = digitalio.DigitalInOut(board.A5)
downButton.switch_to_input(pull=digitalio.Pull.UP)
usb_hid.enable((usb_hid.Device.KEYBOARD,usb_hid.Device.MOUSE,))
if not upButton.value or not downButton.value:
    storage.disable_usb_drive()
    usb_cdc.disable()