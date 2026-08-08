# 🖥️ Screen Popup

A lightweight Windows desktop startup application built with **Python and PySide6** that displays an animated popup in the top-right corner of the screen when Windows starts.

The popup smoothly appears from the top of the screen, displays a personalized greeting inside a speech bubble, waits for a few seconds, and then disappears automatically.

---

## ✨ Features

- 🖥️ Animated desktop popup
- 📍 Appears in the top-right corner of the screen
- 🪟 Transparent, frameless overlay
- 💬 Speech bubble with personalized text
- 🎨 Custom fonts and styling
- ⬇️ Smooth entrance animation
- 💨 Fade-in/fade-out effects
- ⬆️ Smooth exit animation
- 🚀 Automatically launches when Windows starts
- ❌ Automatically closes after the animation
- 📦 Can be packaged as a standalone `.exe`
- 💾 Does not continuously run in the background

---

## 🛠️ Technologies Used

- **Python**
- **PySide6**
- **Qt Animations**
- **PyInstaller**
- **Windows Task Scheduler**

---

## 📁 Project Structure

```
ScreenPopup/
│
├── assets/
│   ├── popup_image.jpg
│   └── second_popup_image.png
│
├── config.py
├── main.py
├── ui/
    └── overlay.py
├── resources.py
│
├── build/
├── dist/
│   └── main.exe
│
├── main.spec
└── README.md
```

---

## 🎬 How It Works

When Windows starts and the user logs in, Windows Task Scheduler launches the application.

The animation follows this sequence:

```
Windows Login
      ↓
Task Scheduler launches application
      ↓
Popup slides down from the top
      ↓
Speech bubble fades in
      ↓
Personalized greeting is displayed
      ↓
Waits for a few seconds
      ↓
Speech bubble fades out
      ↓
Popup slides back up
      ↓
Application closes
```

---

## 🖥️ Desktop Overlay

The application uses a transparent and frameless PySide6 window.

This allows the popup to appear directly over the desktop without displaying a traditional application window.

The overlay uses:

```
Qt.FramelessWindowHint
```

and:

```
Qt.WindowStaysOnTopHint
```

to keep the popup above other windows.

---

