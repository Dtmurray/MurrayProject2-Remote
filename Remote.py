import tkinter as tk
from tkinter import ttk

image_paths = [
    "images/image1.png",
    "images/image2.png",
    "images/image3.png",
    "images/image4.png",
    "images/image5.png"
]
current_image_index = 0
current_volume = 5
is_power_on = True
is_muted = False

def update_image_label():
    if is_power_on:
        photo = tk.PhotoImage(file=image_paths[current_image_index])
        image_label.config(image=photo)
        image_label.image = photo
    else:
        photo = tk.PhotoImage(file="images/imageOFF.png")
        image_label.config(image=photo)
        image_label.image = photo


def change_channel(up=True):
    global current_image_index
    if is_power_on:
        current_image_index = (current_image_index + 1) % len(image_paths) if up else (current_image_index - 1) % len(image_paths)
        update_image_label()

def toggle_mute():
    global is_muted
    is_muted = not is_muted
    update_interface()

def power_toggle():
    global is_power_on
    is_power_on = not is_power_on
    update_interface()

def update_volume(val):
    global current_volume
    current_volume = int(val)
    if is_power_on and not is_muted:
        volume_scale.set(current_volume)

def increment_volume():
    if current_volume < 10:
        update_volume(current_volume + 1)

def decrement_volume():
    if current_volume > 0:
        update_volume(current_volume - 1)

def update_interface():
    state = 'normal' if is_power_on and not is_muted else 'disabled'
    volume_scale.config(state=state)
    vol_up_button.config(state=state)
    vol_down_button.config(state=state)
    mute_button.config(state='normal' if is_power_on else 'disabled')
    ch_up_button.config(state='normal' if is_power_on else 'disabled')
    ch_down_button.config(state='normal' if is_power_on else 'disabled')
    update_image_label()

#GUI
root = tk.Tk()
root.title("TV Remote")
root.resizable(False, False)

image_label = tk.Label(root)
image_label.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

#Buttons
ch_up_button = tk.Button(root, text="Channel +", command=lambda: change_channel(True))
ch_down_button = tk.Button(root, text="Channel -", command=lambda: change_channel(False))
mute_button = tk.Button(root, text="Mute", command=toggle_mute)
power_button = tk.Button(root, text="Power", command=power_toggle)
vol_up_button = tk.Button(root, text="Volume +", command=increment_volume)
vol_down_button = tk.Button(root, text="Volume -", command=decrement_volume)
#Placement of Said Buttons
ch_up_button.grid(row=1, column=5, padx=5, pady=5)
ch_down_button.grid(row=2, column=5, padx=5, pady=5)
mute_button.grid(row=1, column=4, padx=5, pady=5)
power_button.grid(row=1, column=1, padx=5, pady=5)
vol_up_button.grid(row=1, column=0, padx=5, pady=5)
vol_down_button.grid(row=2, column=0, padx=5, pady=5)

# Frame for Slider
volume_frame = tk.Frame(root)
volume_frame.grid(row=2, column=1, columnspan=4, padx=5, pady=5, sticky="ew")

# Volume Slider
volume_scale = ttk.Scale(volume_frame, from_=0, to=10, orient="horizontal", command=update_volume)
volume_scale.set(current_volume)
volume_scale.pack(fill='x', expand=True)

# Volume Level Numbers
label_0 = tk.Label(volume_frame, text="0")
label_5 = tk.Label(volume_frame, text="5")
label_10 = tk.Label(volume_frame, text="10")
label_0.pack(side='left')
label_5.pack(side='left', expand=True)
label_10.pack(side='left')

update_interface()
root.mainloop()
