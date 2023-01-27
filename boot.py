import board
import digitalio
import storage
import usb_cdc
import usb_hid
downLow = digitalio.DigitalInOut(board.A2)
downLow.direction = digitalio.Direction.OUTPUT
downLow.value = False
upButton = digitalio.DigitalInOut(board.D10)
upButton.switch_to_input(pull=digitalio.Pull.DOWN)
downButton = digitalio.DigitalInOut(board.A4)
downButton.switch_to_input(pull=digitalio.Pull.UP)
usb_hid.enable((usb_hid.Device.KEYBOARD,))
if not upButton.value and downButton.value:
    storage.disable_usb_drive()
    usb_cdc.disable()
