"""
Simple 3 axes, 1 button Joystick
Based on JoystickXL Example #1

* Button aon pin GP3
* Axes are on pins AA0, A1, A2

Don't forget to copy boot.py from the example folder to your CIRCUITPY drive.
"""

import config  # type: ignore (this is a CircuitPython built-in)
from joystick_xl.inputs import Axis, Button
from joystick_xl.joystick import Joystick

joystick = Joystick()

joystick.add_input(
    Button(config.button1),
    Axis(config.axis1, deadband=1000),
    Axis(config.axis2, deadband=1000),
    Axis(config.axis3, deadband=1000)
)

while True:
    joystick.update()


