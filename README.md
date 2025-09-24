# 🧃 Sip-n-Stretch

This is my first app project, made using Python. I made this to practice what I learned and out of curiosity.
Also I made this app to help me and my wife stay hydrated, take mindful breaks, and start our day with a motivational boost!
I hope this app would be useful for you too.

## 🌟 Features

- ⏱️ **Hydration Reminder**: Get a popup every 15 minutes to take a sip of water.
- 🧘 **Break Reminder**: After 2 hours of work or study, it nudges you to stretch and take a rest.
- 💬 **Daily Motivation**: If the app runs at startup, it greets you with a motivational message to start your day right.
- 🧪 **System Tray Integration**: Runs quietly in the background
- 🐍 Built with Python and Tkinter, packaged with PyInstaller.

## 📦 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/nerunerun/sip-n-stretch.git
   cd sip-n-stretch

2. Run the app
   - If you're using the .pkg installer, just double-click it.
   - Or run the Python script directly:
     python reminder_app.py

## 🧙 Tech Stack
- Python 3.x
- Tkinter
- win10toast or plyer for notifications
- PyInstaller for packaging

## 🧁 Folder Structure
```bash
sip-n-stretch/
├── assets/              # Tray icon and other images
├── build/               # PyInstaller build files
├── reminder_app/        # Main app code
│   ├── reminder_app.py
│   └── ...
├── README.md
└── reminder_app.pkg     # Installer file
