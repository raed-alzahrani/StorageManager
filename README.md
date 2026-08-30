# Storage Manager & Organizer

A high-performance desktop storage inspection and directory organizer built with Python and CustomTkinter. Designed to quickly identify disk space consumers and organize files with keyboard-driven workflows.

---

## Features

- **Multi-Level Parallel Scanner:** Deep recursive folder sizing powered by a multi-threaded queue worker that scales across all CPU threads.
- **Configurable Performance Profiles:** Toggle on the fly between **Normal** (balanced I/O) and **Extreme** (full parallel throughput for high-speed NVMe drives).
- **Persistent Disk Caching:** Stores file timestamps (`mtime`) and calculated sizes to skip rescanning unmodified directory trees instantly.
- **Dynamic Sorting:** Sort items by space consumed (Largest / Smallest), alphabetical names (A-Z), or file extensions.
- **Keyboard-Centric Navigation:** Smooth WASD and arrow key navigation with zero input latency and responsive viewport scrolling.
- **Clipboard Operations:** Select items, cut with `Ctrl+X`, navigate to any directory, and paste with `Ctrl+V`.
- **Automated Categorization:** One-click sorting of loose files into structured categories (Images, Documents, Media, Code, Archives).
- **Modern Adaptive UI:** Built with CustomTkinter featuring clean accent palettes and Dark/Light modes.

---

## Keyboard Controls & Shortcuts

| Key / Shortcut | Action |
| :--- | :--- |
| `W` / `Up Arrow` | Move focus up |
| `S` / `Down Arrow` | Move focus down |
| `A` / `Left Arrow` / `Backspace` | Navigate to parent directory (Up) |
| `D` / `Right Arrow` | Open selected directory |
| `Enter` / `Space` | Toggle checkbox selection |
| `Ctrl + X` | Cut selected items to clipboard |
| `Ctrl + V` | Paste / Move clipboard items to current directory |

---

## Installation & Setup

1. **Clone the repository:**
    git clone https://github.com/raed-alzahrani/StorageManager.git
    cd StorageManager

2. **Install dependencies:**
    pip install -r requirements.txt

3. **Run the application:**
    python main.pyw

    *(On Windows, you can double-click `main.pyw` directly without opening a terminal window).*

---

## Requirements

- Python 3.8+
- customtkinter >= 5.2.0
- pillow >= 10.0.0
- tkinterdnd2 >= 0.3.0

---

## License

Licensed under the MIT License (LICENSE).
