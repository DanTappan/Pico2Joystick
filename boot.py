import usb_hid
import time
from joystick_xl.hid import create_joystick
import storage
import digitalio
import config

# disable storage if joystick button not pressed
# hold down button for 5 seconds after plugging in USB
time.sleep(5)
with digitalio.DigitalInOut(config.button1) as button:
    # Button push grounds
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP

    # Disable devices only if button is not pressed.
    if button.value:
        print("Disabled storage")
        storage.disable_usb_drive()
    else:
        print("Enable storage")

usb_hid.set_interface_name(config.usb_name)

# enable default CircuitPython USB HID devices as well as JoystickXL
usb_hid.enable(
  (
    #usb_hid.Device.KEYBOARD,
    #usb_hid.Device.MOUSE,
    #usb_hid.Device.CONSUMER_CONTROL,
    create_joystick(axes=3, buttons=1, hats=0),
  )
)


print("Boot done")