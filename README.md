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

## 🎞️ Animation

The popup uses Qt's property animation system:

```
QPropertyAnimation
```

to smoothly move the overlay onto and off the screen.

Easing curves are used to make the movement feel smoother:

```
QEasingCurve.OutCubic
```

and:

```
QEasingCurve.InCubic
```

The speech bubble uses:

```
QGraphicsOpacityEffect
```

to create fade-in and fade-out effects.

---

💬 Personalized Greeting

The text displayed inside the popup can easily be customized.

For example:

```
self.greeting = QLabel(
    "What's up,\nUser!",
    self.bubble
)
```

The greeting can be changed to any custom message.

---

## 📦 Run the Project

1. Install Python

Check whether Python is installed:

```
python --version
```

2. Install PySide6

```
pip install PySide6
```

3. Run the application

From the project directory:

```
python main.py
```

---

## 📦 Building the EXE

Install PyInstaller:

```
pip install pyinstaller
```

Build the application:

```
pyinstaller --onefile --windowed --add-data "assets;assets" main.py
```

The executable will be created inside:

```
dist/main.exe
```

---

## 🔧 Resource Handling

The project uses a resource helper to correctly locate assets when running both from Python and from a PyInstaller executable.

Example:

```
from resources import resource_path
```

Assets can then be loaded using:

```
QPixmap(
    resource_path("assets/popup_image.jpg")
)
```

This ensures that images continue to work after packaging the application as an .exe.

---

## 🚀 Windows Startup

The application uses Windows Task Scheduler to launch automatically when the user logs into Windows.

Task Configuration

Task Name:
ScreenPopup

Trigger:
At log on

Action:
Start main.exe

Run:
Only when user is logged on

This allows the popup to appear automatically without manually running the program.

---

## 🧹 Application Lifetime

The application is designed to run only for the duration of the popup animation.

After the animation finishes, the application closes:

```
self.upAnimation.finished.connect(self.close)
```

Therefore, it does not continuously run in the background.

```
Windows Login
      ↓
Application starts
      ↓
Popup animation
      ↓
Application closes
      ↓
No background process
```

The Task Scheduler entry remains registered so the application can run again at the next login.

---

## 💾 Performance

The application is designed to have minimal impact on system performance.

It:

Uses minimal CPU while the animation is running
Uses a small amount of RAM
Does not continuously run in the background
Automatically exits after the animation
Uses lightweight image assets

The application only consumes resources for a short period during startup.

---

