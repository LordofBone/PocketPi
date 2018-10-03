#!/usr/bin/env python
#Original script from Pimoroni and modified by me for different functions
#https://github.com/pimoroni/touch-phat

import os
import signal
import subprocess
#from sys import exit, version_info

import touchphat


try:
    os.environ['DISPLAY']
    print("""

Touch pHAT: App Launcher Example

A: Terminal
B: Browser
C: Guake
D: Keyboard

Back: Reboot
Enter: Shutdown

Press Ctrl+C to exit!
""")
except:
    print("""
No X display detected!
This example requires a full desktop
... exiting.
""")
    exit()


# reboot
@touchphat.on_release('Back')
def handle_touch(event):
    os.system("reboot")

# simple use of os.system to launch a terminal window
@touchphat.on_release('A')
def handle_touch(event):
    os.system("x-terminal-emulator &")
    print("New terminal")

# use of xdg-open to open in preferred browser application
@touchphat.on_release('B')
def handle_touch(event):
    os.system("xdg-open 'https://www.google.com' &")
    print("Browser launched")

# launch guake
@touchphat.on_release('C')
def handle_touch(event):
    os.system("guake &")
    print("Guake launched")

# launch on screen keyboard
@touchphat.on_release('D')
def handle_touch(event):
    os.system("xvkbd &")
    print("Keyboard launched")

# shutdown
@touchphat.on_release('Enter')
def handle_touch(event):
    subprocess.check_call(["sudo shutdown now"], shell=True)

signal.pause()
