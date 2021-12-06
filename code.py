# Based on the Gist created by wildestpixel at https://gist.github.com/wildestpixel/6b684b8bc886392f7c4c57015fab3d97

import time
import board
import busio
import usb_hid

from adafruit_bus_device.i2c_device import I2CDevice
import adafruit_dotstar

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

from digitalio import DigitalInOut, Direction, Pull
cs = DigitalInOut(board.GP17)
cs.direction = Direction.OUTPUT
cs.value = 0
num_pixels = 16
pixels = adafruit_dotstar.DotStar(board.GP18, board.GP19, num_pixels, brightness=0.1, auto_write=True)
i2c = busio.I2C(board.GP5, board.GP4)
device = I2CDevice(i2c, 0x20)
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
def colourwheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)
def read_button_states(x, y):
    pressed = [0] * 16
    with device:
        device.write(bytes([0x0]))
        result = bytearray(2)
        device.readinto(result)
        b = result[0] | result[1] << 8
        for i in range(x, y):
            if not (1 << i) & b:
                pressed[i] = 1
            else:
                pressed[i] = 0
    return pressed
held = [0] * 16
while True:
    pressed = read_button_states(0, 16)

    if pressed[0]:
        pixels[0] = (255, 255, 255)  # Turns the pressed button white while the command is running

        # Write email sign-off and send (specific to Microsoft Outlook)
        if not held[0]:
            kbd.send(Keycode.ENTER)
            kbd.send(Keycode.ENTER)
            layout.write("Kind regards,")
            kbd.send(Keycode.ENTER)
            kbd.send(Keycode.ENTER)
            kbd.send(Keycode.ENTER)
            layout.write("Matt")
            time.sleep(1)
            kbd.send(Keycode.ALT, Keycode.S)
            #held[0] = 1

    elif pressed[1]:
        pixels[1] = (255, 255, 255)  # Turns the pressed button white while the command is running
        
        # Open Teams from Start Menu
        if not held[1]:
            kbd.send(Keycode.GUI)  # Win key
            time.sleep(1)
            layout.write("Teams")
            time.sleep(1)
            kbd.send(Keycode.ENTER)
            held[1] = 1

    elif pressed[2]:
        pixels[2] = (255, 255, 255)  # Turns the pressed button white while the command is running

        # Launch Outlook (the fifth app in the taskbar)
        if not held[2]:
            kbd.send(Keycode.GUI, Keycode.FIVE) # Win + 5
            held[2] = 1

    elif pressed[3]:
        pixels[3] = (255, 255, 255)  # Turns the pressed button white while the command is running

        # Open PowerShell from run dialogue and run test command
        if not held[3]:
            kbd.send(Keycode.GUI, Keycode.EIGHT) # Launches the eighth application pinned in the Windows taskbar.
            time.sleep(1)
            layout.write("plink office")
            time.sleep(1)
            kbd.send(Keycode.ENTER)
            time.sleep(1)
            layout.write("[password]") # Currently a hardcoded password until this is moved to certificate based auth
            time.sleep(1)
            kbd.send(Keycode.ENTER)
            time.sleep(1)
            kbd.send(Keycode.ENTER)
            time.sleep(1)
            layout.write("cd Round-LCD-HAT")
            time.sleep(1)
            kbd.send(Keycode.ENTER)
            layout.write("python3 ../Flask/server.py")
            time.sleep(1)
            kbd.send(Keycode.ENTER)
            held[3] = 1

    elif pressed[4]:
        pixels[4] = (255, 255, 255)  # Turns the pressed button white while the command is running
        
        # Qualys search query written in Qualys Query Language (QQL) 
        if not held[4]:
            layout.write("vulnerabilities.status:FIXED and vulnerabilities.lastFound:[now-1w ... now-1s]")
            kbd.send(Keycode.ENTER)
            #held[4] = 1
            
    elif pressed[5]:
        pixels[5] = colourwheel(5 * 16)  # Map pixel index to 0-255 range

        if not held[5]:
            layout.write("Unassigned key")
            kbd.send(Keycode.ENTER)
            held[5] = 1

    elif pressed[6]:
        pixels[6] = colourwheel(6 * 16)  # Map pixel index to 0-255 range

        if not held[6]:
            layout.write("Unassigned key")
            kbd.send(Keycode.ENTER)
            held[6] = 1
    
    elif pressed[7]:
        pixels[7] = colourwheel(7 * 16)  # Map pixel index to 0-255 range

        if not held[7]:
            layout.write("Unassigned key")
            kbd.send(Keycode.ENTER)
            held[7] = 1

    elif pressed[8]:
        pixels[8] = colourwheel(8 * 16)  # Map pixel index to 0-255 range

        if not held[8]:
            layout.write("Unassigned key")
            kbd.send(Keycode.ENTER)
            held[8] = 1
            
    elif pressed[9]:
        pixels[9] = colourwheel(9 * 16)  # Map pixel index to 0-255 range

        if not held[9]:
            layout.write("Unassigned key")
            kbd.send(Keycode.ENTER)
            held[9] = 1

    elif pressed[10]:
        pixels[10] = colourwheel(10 * 16)  # Map pixel index to 0-255 range

        if not held[10]:
            layout.write("Unassigned key")
            kbd.send(Keycode.ENTER)
            held[10] = 1
            
    elif pressed[11]:
        pixels[11] = colourwheel(11 * 16)  # Map pixel index to 0-255 range

        if not held[11]:
            layout.write("Unassigned key")
            kbd.send(Keycode.ENTER)
            held[11] = 1

    elif pressed[12]:
        pixels[12] = colourwheel(12 * 16)  # Map pixel index to 0-255 range

        if not held[12]:
            layout.write("Unassigned key")
            kbd.send(Keycode.ENTER)
            held[12] = 1
            
    elif pressed[13]:
        pixels[13] = colourwheel(13 * 16)  # Map pixel index to 0-255 range

        if not held[13]:
            layout.write("Unassigned key")
            kbd.send(Keycode.ENTER)
            held[13] = 1

    elif pressed[14]:
        pixels[14] = colourwheel(14 * 16)  # Map pixel index to 0-255 range

        if not held[14]:
            layout.write("Unassigned key")
            kbd.send(Keycode.ENTER)
            held[14] = 1
            
    elif pressed[15]:
        pixels[15] = colourwheel(15 * 16)  # Map pixel index to 0-255 range

        if not held[15]:
            layout.write("Unassigned key")
            kbd.send(Keycode.ENTER)
            held[15] = 1
    
    else:  # Released state
        for i in range(16):
            pixels[i] = colourwheel(i * 16)
            held[i] = 0  # Set held states to off
        time.sleep(0.1) # Debounce
