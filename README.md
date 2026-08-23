# Storage Manager & Organizer

A high-performance desktop storage inspection and directory organizer built with Python and CustomTkinter. Designed to quickly identify disk space consumers and organize files with keyboard-driven workflows.

---

## Features

- **Ultra-Fast Disk Sizing:** Multi-threaded iterative directory scanner engineered to bypass Windows NTFS junction loops and reparse points smoothly.
- **Smart Space Filtering:** Automatically ignores empty or negligible items (< 1 KB) to focus only on actual space consumers.
- **Dynamic Sorting:** Sort items by space consumed (Largest / Smallest), alphabetical names (A-Z), or file extensions.
- **Keyboard-Centric Navigation:** Full directional navigation using WASD or arrow keys with viewport auto-scroll.
- **Clipboard Move (Cut & Paste):** Select items, cut with `Ctrl+X`, navigate to any directory, and paste with `Ctrl+V`.
- **Automated Categorization:** One-click organization of raw files into structured categories (Images, Documents, Media, Code, Archives, etc.).
- **Modern Adaptive UI:** Built with CustomTkinter featuring custom color accents and Dark/Light modes.

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
   ```bash
   git clone https://github.com/raed-alzahrani/StorageManager.git
   cd StorageManager
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python main.pyw
   ```
   *(On Windows, you can double-click `main.pyw` directly without opening a terminal window).*