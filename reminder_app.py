# Import necessary libraries
import tkinter as tk
import threading
import time
import random
import os
import sys
from pystray import Icon, MenuItem, Menu
from PIL import Image

# Messages list
messages = [
    "How are you today?",
    "Are you ready to start a good day?",
    "Let's start the day with a smile",
    "God will help you do what you need to do today!"
]

# ✅ Create a hidden root window for Tkinter
hidden_root = tk.Tk()
hidden_root.withdraw()

# Function to show a popup bubble with a message
def show_popup(msg=None):
    def popup():
        # Window size
        win_w, win_h = 250, 120

        # Create popup window
        root = tk.Toplevel(hidden_root)
        root.overrideredirect(True)
        root.attributes("-topmost", True)
        root.after(10000, root.destroy)  # Auto-close after 10 seconds

        # Random position on screen
        screen_w = root.winfo_screenwidth()
        screen_h = root.winfo_screenheight()
        x = random.randint(0, screen_w - win_w)
        y = random.randint(0, screen_h - win_h)
        root.geometry(f"{win_w}x{win_h}+{x}+{y}")

        # Choose a random message if none provided
        msg_to_show = msg if msg else random.choice(messages)

        # Create canvas for rounded bubble
        canvas = tk.Canvas(root, width=win_w, height=win_h, bg="white", highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        def draw_rounded_bubble(x1, y1, x2, y2, r=20, color="#e0f7fa"):
            canvas.create_arc(x1, y1, x1+r*2, y1+r*2, start=90, extent=90, fill=color, outline=color)
            canvas.create_arc(x2-r*2, y1, x2, y1+r*2, start=0, extent=90, fill=color, outline=color)
            canvas.create_arc(x1, y2-r*2, x1+r*2, y2, start=180, extent=90, fill=color, outline=color)
            canvas.create_arc(x2-r*2, y2-r*2, x2, y2, start=270, extent=90, fill=color, outline=color)
            canvas.create_rectangle(x1+r, y1, x2-r, y2, fill=color, outline=color)
            canvas.create_rectangle(x1, y1+r, x2, y2-r, fill=color, outline=color)

        draw_rounded_bubble(10, 10, win_w-10, win_h-10)

        canvas.create_text(
            win_w//2, win_h//2,
            text=msg_to_show,
            font=("Comic Sans MS", 11),
            width=win_w-40,
            justify="center"
        )

        close_btn = tk.Button(root, text="✕", command=root.destroy, bd=0, bg="white", fg="black", font=("Arial", 9))
        close_btn.place(x=win_w-20, y=5, width=15, height=15)

    # ✅ Schedule popup safely in the Tkinter mainloop
    hidden_root.after(0, popup)

# Background loop to trigger reminders
def reminder_loop():
    last_water = time.time()
    last_break = time.time()
    while True:
        now = time.time()
        if now - last_water >= 900:  # 15 minutes
            show_popup("Time to drink 🥛")
            last_water = now
        if now - last_break >= 7200:  # 2 hours
            show_popup("Take a break ☕")
            last_break = now
        time.sleep(10)

# Create system tray icon using ICHTHUS.ico
def create_tray_icon():
    try:
        # Detect base path (works for both exe and script)
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(__file__)

        icon_path = os.path.join(base_path, "ICHTHUS.ico")

        icon = Icon("Reminder", Image.open(icon_path), menu=Menu(
            MenuItem("Quit", lambda icon, item: icon.stop())
        ))

        # Start reminder loop in background
        threading.Thread(target=reminder_loop, daemon=True).start()

        # Show a random message immediately to confirm it's running
        show_popup(random.choice(messages))

        # Run tray icon in its own thread
        threading.Thread(target=icon.run, daemon=True).start()

    except Exception as e:
        print("Tray icon failed:", e)
        show_popup("App started, but tray icon failed ❗")

# Start the app
create_tray_icon()

# ✅ Keep the Tkinter event loop running
hidden_root.mainloop()