from pynput import keyboard
from datetime import datetime
import os

file_path = 'output.txt'

# Define the key codes for F13 to F24 for keys I need
special_keys = {'St': keyboard.Key.f13,
                'Hl': keyboard.Key.f14,
                'Ct': keyboard.Key.f15,
                'En': keyboard.Key.f16,
                'Bg': keyboard.Key.f21,
                'Eg': keyboard.Key.f22,
                }

special_old_pairs = {'St': " Numpad6 ",
                'Hl': " Numpad7 ",
                'Ct': " Numpad8 ",
                'En': " Numpad9 ",
                'Bg': " Numpad1 ",
                'Eg': " Numpad2 ",
                }

#Check if Output.txt currently exists, back it up with date of backup
if os.path.exists(file_path):
    os.rename(file_path, 'output_' + str(datetime.now().strftime("%I:%M:%S")).replace(':','-') + '.txt')
    #os.remove(file_path)

def write_line(stamp):
    with open(file_path, 'a') as file:
        file.write(stamp)

def on_press(key):
    if key in special_keys.values():
        print('key {0} pressed'.format(
             key))
        inverted_special_keys = {v: k for k, v in special_keys.items()}
        desired_key = inverted_special_keys[key]
        print(desired_key)
        current_time = datetime.now()
        formatted_time = current_time.strftime("%I:%M:%S")
        write_line(special_old_pairs[desired_key] + desired_key + " " + formatted_time + "\n")

# Setting up the listener
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()