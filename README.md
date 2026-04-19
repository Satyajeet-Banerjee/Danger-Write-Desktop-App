# ⚠️ DangerWrite Desktop App

A distraction-based desktop writing application built using **Python and PyQt5**, inspired by “The Most Dangerous Writing App”.

If you stop typing for more than a few seconds, **your entire text is automatically deleted**, forcing continuous writing flow.

---

## 🚀 Features

- 🧠 Real-time typing detection
- ⏱️ Auto-reset inactivity timer (5 seconds)
- 💀 Automatic text deletion on inactivity
- 🖥️ Desktop GUI application (PyQt5)
- 🎯 Minimal distraction writing environment
- ⚡ Event-driven architecture

---

## 🛠️ Tech Stack

- Python 🐍
- PyQt5 (GUI framework)
- QTimer (event-based timing system)

---

## 🧠 How It Works

- The application listens to user typing events.
- Every keystroke resets a 5-second timer.
- If no input is detected within 5 seconds:
  - The text area is cleared automatically.
- This creates a continuous writing pressure system to improve focus and productivity.

---

## 🏗️ Project Architecture

This project follows a **modular MVC-inspired structure**:


---

## 🖥️ How to Run

### 1. Install dependencies
bash
pip install PyQt5
python main.py
