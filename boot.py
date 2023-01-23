import board
import digitalio
import storage
import usb_cdc
import usb_hid
upLow = digitalio.DigitalInOut(board.D12)
upLow.direction = digitalio.Direction.OUTPUT
upLow = False
downLow = digitalio.DigitalInOut(board.A3)
downLow.direction = digitalio.Direction.OUTPUT
downLow = False
upButton = digitalio.DigitalInOut(board.D10)
upButton.switch_to_input(pull=digitalio.Pull.UP)
downButton = digitalio.DigitalInOut(board.A5)
downButton.switch_to_input(pull=digitalio.Pull.UP)
usb_hid.enable((usb_hid.Device.KEYBOARD,))
if upButton.value and downButton:
    storage.disable_usb_drive()
    usb_cdc.disable()