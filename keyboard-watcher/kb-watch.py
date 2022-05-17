from pynput import keyboard
#(https://pynput.readthedocs.io/en/latest/keyboard.html)

#active modifiers
current = set()

#Hotkey Combinations
COMBINATIONS = [
{keyboard.KeyCode(vk=96)}, # Numpad 0
{keyboard.KeyCode(vk=111)} # Numpad Divide
]



def execute():
    print("You pressed something on the number pad")

    #set up keyboard listener
def on_press(key):
        if any([key in COMBO for COMBO in COMBINATIONS]):
            current.add(key)
            if any(all(k in current for k in COMBO) for COMBO in COMBINATION):
                execute()

def on_release(key):
     if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
