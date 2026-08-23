import os
import sys
import json
import time
import shutil
import threading
from concurrent.futures import ThreadPoolExecutor
import tkinter as tk
from tkinter import filedialog, messagebox

# Auto-check dependencies
REQUIRED_LIBS = {
    "customtkinter": "customtkinter",
    "PIL": "pillow"
}

missing = []
for mod, pkg in REQUIRED_LIBS.items():
    try:
        __import__(mod)
    except ImportError:
        missing.append(pkg)

if missing:
    root = tk.Tk()
    root.title("Missing Dependencies")
    root.geometry("450x260")
    root.resizable(False, False)
    root.configure(bg="#0b0f17")

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    root.geometry(f"450x260+{int((ws-450)/2)}+{int((hs-260)/2)}")

    tk.Label(root, text="Missing Python Packages", font=("Segoe UI", 12, "bold"), fg="#f87171", bg="#0b0f17").pack(pady=(20, 5))
    tk.Label(root, text="The following packages are required to run the application:", font=("Segoe UI", 9), fg="#94a3b8", bg="#0b0f17").pack()

    box = tk.Frame(root, bg="#121926", bd=1, relief="solid")
    box.pack(fill="x", padx=30, pady=10)
    for pkg in missing:
        tk.Label(box, text=f"• {pkg}", font=("Consolas", 10, "bold"), fg="#10b981", bg="#121926").pack(anchor="w", padx=12, pady=2)

    def install_pkgs():
        root.destroy()
        py_exe = sys.executable
        if py_exe.lower().endswith("pythonw.exe"):
            py_exe = py_exe[:-10] + "python.exe"

        script_path = os.path.abspath(__file__)
        bat_cmd = f"""@echo off
title Installing Dependencies...
echo [*] Installing: {" ".join(missing)}
"{py_exe}" -m pip install --upgrade pip {" ".join(missing)}
echo.
echo [*] Launching application...
start "" "{sys.executable}" "{script_path}"
exit
"""
        bat_file = os.path.join(os.environ.get("TEMP", "."), "_install_storage_deps.bat")
        with open(bat_file, "w", encoding="utf-8") as f:
            f.write(bat_cmd)

        subprocess.Popen(f'start "" "{bat_file}"', shell=True)
        sys.exit()

    btns = tk.Frame(root, bg="#0b0f17")
    btns.pack(fill="x", padx=30, pady=(10, 15))
    tk.Button(btns, text="Cancel", font=("Segoe UI", 9), bg="#1e293b", fg="#fff", bd=0, padx=14, pady=5, command=sys.exit).pack(side="left")
    tk.Button(btns, text="Install Now", font=("Segoe UI", 9, "bold"), bg="#10b981", fg="#042f2e", bd=0, padx=14, pady=5, command=install_pkgs).pack(side="right")

    root.mainloop()
    sys.exit()

from PIL import Image
import customtkinter as ctk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")

CATEGORY_RULES = {
    "Images": ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.svg', '.ico', '.tiff'],
    "Documents": ['.pdf', '.docx', '.doc', '.xlsx', '.xls', '.pptx', '.ppt', '.txt', '.csv', '.rtf', '.md'],
    "Media_Videos": ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm'],
    "Media_Audio": ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma'],
    "Archives": ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.iso'],
    "Executables": ['.exe', '.msi', '.bat', '.cmd', '.apk', '.jar'],
    "Code": ['.py', '.pyw', '.js', '.html', '.css', '.cpp', '.c', '.cs', '.java', '.json', '.xml', '.sql', '.php', '.ts']
}

FONT_PROFILES = {
    "Futuristic (Bahnschrift)": {
        "title": ("Bahnschrift", 16, "bold"), "ui_bold": ("Bahnschrift", 12, "bold"),
        "ui_sm": ("Bahnschrift", 11, "bold"), "row_main": ("Bahnschrift", 12, "bold"),
        "badge": ("Consolas", 10, "bold"), "mono": ("Consolas", 11, "bold")
    },
    "Modern Heavy (Segoe UI)": {
        "title": ("Segoe UI", 16, "bold"), "ui_bold": ("Segoe UI", 12, "bold"),
        "ui_sm": ("Segoe UI", 11, "bold"), "row_main": ("Segoe UI", 12, "bold"),
        "badge": ("Consolas", 10, "bold"), "mono": ("Consolas", 11, "bold")
    },
    "Cyber Terminal (Cascadia Mono)": {
        "title": ("Cascadia Mono", 15, "bold"), "ui_bold": ("Cascadia Mono", 11, "bold"),
        "ui_sm": ("Cascadia Mono", 10, "bold"), "row_main": ("Cascadia Mono", 11, "bold"),
        "badge": ("Cascadia Mono", 10, "bold"), "mono": ("Cascadia Mono", 10, "bold")
    },
    "Arcade Punch (Trebuchet MS)": {
        "title": ("Trebuchet MS", 16, "bold"), "ui_bold": ("Trebuchet MS", 12, "bold"),
        "ui_sm": ("Trebuchet MS", 11, "bold"), "row_main": ("Trebuchet MS", 12, "bold"),
        "badge": ("Consolas", 10, "bold"), "mono": ("Consolas", 11, "bold")
    },
    "Clean Solid (Arial)": {
        "title": ("Arial", 16, "bold"), "ui_bold": ("Arial", 12, "bold"),
        "ui_sm": ("Arial", 11, "bold"), "row_main": ("Arial", 12, "bold"),
        "badge": ("Consolas", 10, "bold"), "mono": ("Consolas", 11, "bold")
    }
}

THEMES = {
    "Emerald": {
        "primary": "#10b981", "hover": "#059669", "btn_bg": "#064e3b", "btn_hover": "#047857",
        "menu_bg": "#064e3b", "menu_btn": "#10b981", "menu_hover": "#059669",
        "focus_dark": "#132724", "focus_border": "#10b981", "focus_light": "#e6fffa",
        "badge_dark": "#0c2822", "badge_text_dark": "#34d399", "badge_light": "#d1fae5", "badge_text_light": "#065f46"
    },
    "Nordic Blue": {
        "primary": "#38bdf8", "hover": "#0284c7", "btn_bg": "#0c4a6e", "btn_hover": "#0369a1",
        "menu_bg": "#0c4a6e", "menu_btn": "#38bdf8", "menu_hover": "#0284c7",
        "focus_dark": "#102538", "focus_border": "#38bdf8", "focus_light": "#e0f2fe",
        "badge_dark": "#0e2c45", "badge_text_dark": "#7dd3fc", "badge_light": "#e0f2fe", "badge_text_light": "#0369a1"
    },
    "Amethyst": {
        "primary": "#c084fc", "hover": "#9333ea", "btn_bg": "#581c87", "btn_hover": "#6b21a8",
        "menu_bg": "#581c87", "menu_btn": "#c084fc", "menu_hover": "#9333ea",
        "focus_dark": "#231836", "focus_border": "#c084fc", "focus_light": "#f3e8ff",
        "badge_dark": "#2e1845", "badge_text_dark": "#d8b4fe", "badge_light": "#f3e8ff", "badge_text_light": "#6b21a8"
    }
}

THEME_MIGRATION = {
    "Green": "Emerald",
    "Blue": "Nordic Blue",
    "Purple": "Amethyst"
}

def format_size(bytes_size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:3.1f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.1f} PB"

def calculate_size_ultra_fast(target_path):
    if not os.path.exists(target_path):
        return 0

    try:
        st = os.lstat(target_path)
        if getattr(st, 'st_file_attributes', 0) & 0x400 or os.path.islink(target_path):
            return 0
        if not os.path.isdir(target_path):
            return st.st_size
    except (OSError, PermissionError):
        return 0

    total_bytes = 0
    stack = [target_path]

    while stack:
        current_dir = stack.pop()
        try:
            with os.scandir(current_dir) as entries:
                for entry in entries:
                    try:
                        if entry.is_dir(follow_symlinks=False):
                            stat_res = entry.stat(follow_symlinks=False)
                            if not (stat_res.st_file_attributes & 0x400):
                                stack.append(entry.path)
                        else:
                            total_bytes += entry.stat(follow_symlinks=False).st_size
                    except (PermissionError, OSError):
                        continue
        except (PermissionError, OSError):
            continue

    return total_bytes

class StorageManagerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Storage Manager & Organizer")
        self.minsize(960, 640)

        self.config = self.load_config()
        raw_theme = self.config.get("theme", "Emerald")
        self.current_theme = THEME_MIGRATION.get(raw_theme, raw_theme)
        if self.current_theme not in THEMES:
            self.current_theme = "Emerald"

        self.current_font = self.config.get("font_profile", "Futuristic (Bahnschrift)")
        if self.current_font not in FONT_PROFILES:
            self.current_font = "Futuristic (Bahnschrift)"

        self.appearance_mode = self.config.get("appearance", "Dark")
        self.working_dir = self.config.get("working_dir", BASE_DIR)
        self.current_sort = self.config.get("sort_mode", "Size (Largest First)")

        if not os.path.exists(self.working_dir):
            self.working_dir = BASE_DIR

        ctk.set_appearance_mode(self.appearance_mode)

        saved_geom = self.config.get("geometry", "1000x700")
        try: self.geometry(saved_geom)
        except Exception: self.geometry("1000x700")

        if self.config.get("maximized", False):
            self.after(100, lambda: self.state("zoomed"))

        self.file_vars = {}
        self.row_widgets = []
        self.current_display_items = []
        self.scanned_items_data = []
        self.displayed_count = 100
        self.focused_index = 0
        self.last_key_time = 0
        self.is_scanning = False
        self.cut_clipboard_items = []

        self._apply_appearance_backgrounds()
        self.setup_ui()
        self.apply_theme(self.current_theme)
        self.apply_font(self.current_font)
        self._bind_global_key_events()

        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.refresh_list()

    def load_config(self):
        defaults = {
            "geometry": "1000x700", "maximized": False,
            "theme": "Emerald", "font_profile": "Futuristic (Bahnschrift)",
            "appearance": "Dark", "working_dir": BASE_DIR,
            "sort_mode": "Size (Largest First)"
        }
        if os.path.exists(CONFIG_PATH):
            try:
                with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
                    defaults.update(json.load(f))
            except Exception: pass

        t = defaults.get("theme", "Emerald")
        defaults["theme"] = THEME_MIGRATION.get(t, t if t in THEMES else "Emerald")
        return defaults

    def save_config(self):
        is_zoomed = (self.state() == "zoomed")
        geom = self.config.get("geometry", "1000x700") if is_zoomed else self.geometry()
        self.config = {
            "geometry": geom, "maximized": is_zoomed,
            "theme": self.current_theme, "font_profile": self.current_font,
            "appearance": self.appearance_mode, "working_dir": self.working_dir,
            "sort_mode": self.sort_menu.get()
        }
        try:
            with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2)
        except Exception: pass

    def on_close(self):
        self.save_config()
        self.destroy()

    def _apply_appearance_backgrounds(self):
        if self.appearance_mode == "Dark":
            self.configure(fg_color="#0b0f17")
            self.card_bg = "#121926"
            self.inner_bg = "#080c12"
            self.panel_border = "#1f293d"
            self.text_main = "#f8fafc"
            self.text_muted = "#94a3b8"
        else:
            self.configure(fg_color="#f1f5f9")
            self.card_bg = "#ffffff"
            self.inner_bg = "#f8fafc"
            self.panel_border = "#cbd5e1"
            self.text_main = "#0f172a"
            self.text_muted = "#64748b"

    def setup_ui(self):
        self.header = ctk.CTkFrame(self, fg_color=self.card_bg, corner_radius=12, border_width=1, border_color=self.panel_border)
        self.header.pack(fill="x", padx=16, pady=(12, 4))

        top_row = ctk.CTkFrame(self.header, fg_color="transparent")
        top_row.pack(fill="x", padx=12, pady=(8, 8))

        self.app_title = ctk.CTkLabel(top_row, text="Storage Manager")
        self.app_title.pack(side="left", padx=4)

        ctrls = ctk.CTkFrame(top_row, fg_color="transparent")
        ctrls.pack(side="right")

        self.font_picker = ctk.CTkOptionMenu(ctrls, values=list(FONT_PROFILES.keys()), width=180, height=30, command=self.handle_font_change)
        self.font_picker.set(self.current_font)
        self.font_picker.pack(side="left", padx=3)

        self.theme_picker = ctk.CTkOptionMenu(ctrls, values=list(THEMES.keys()), width=120, height=30, command=self.handle_theme_change)
        self.theme_picker.set(self.current_theme)
        self.theme_picker.pack(side="left", padx=3)

        self.btn_mode_toggle = ctk.CTkButton(ctrls, text="Dark" if self.appearance_mode == "Dark" else "Light", width=75, height=30, fg_color="#1e293b", hover_color="#334155", command=self.toggle_appearance)
        self.btn_mode_toggle.pack(side="left", padx=3)

        self.dir_frame = ctk.CTkFrame(self, fg_color=self.card_bg, corner_radius=10, border_width=1, border_color=self.panel_border)
        self.dir_frame.pack(fill="x", padx=16, pady=4)

        self.btn_up = ctk.CTkButton(self.dir_frame, text="▲ Up", width=70, height=32, fg_color="#1e293b", hover_color="#334155", command=self.navigate_up)
        self.btn_up.pack(side="left", padx=(10, 4), pady=6)

        self.lbl_path = ctk.CTkLabel(self.dir_frame, text="Path:", text_color=self.text_muted)
        self.lbl_path.pack(side="left", padx=(4, 6), pady=6)

        self.entry_path = ctk.CTkEntry(self.dir_frame, height=32, fg_color=self.inner_bg, border_color=self.panel_border, text_color=self.text_main)
        self.entry_path.insert(0, self.working_dir)
        self.entry_path.pack(side="left", fill="x", expand=True, padx=4, pady=6)
        self.entry_path.bind("<Return>", lambda _: self.refresh_list())

        self.btn_browse = ctk.CTkButton(self.dir_frame, text="Browse", width=100, height=32, fg_color="#1e293b", hover_color="#334155", command=self.choose_directory)
        self.btn_browse.pack(side="right", padx=(4, 10), pady=6)

        self.opts_frame = ctk.CTkFrame(self, fg_color=self.card_bg, corner_radius=10, border_width=1, border_color=self.panel_border)
        self.opts_frame.pack(fill="x", padx=16, pady=4)

        self.entry_new_folder = ctk.CTkEntry(self.opts_frame, placeholder_text="New folder name...", fg_color=self.inner_bg, border_color=self.panel_border, height=32, width=190)
        self.entry_new_folder.pack(side="left", padx=(10, 3), pady=6)

        self.btn_move = ctk.CTkButton(self.opts_frame, text="Move", width=80, height=32, command=self.move_selected)
        self.btn_move.pack(side="left", padx=2, pady=6)

        self.btn_cut = ctk.CTkButton(self.opts_frame, text="Cut", fg_color="#1e293b", hover_color="#334155", width=70, height=32, command=self.cut_selected)
        self.btn_cut.pack(side="left", padx=2, pady=6)

        self.btn_paste = ctk.CTkButton(self.opts_frame, text="Paste", fg_color="#1e293b", hover_color="#334155", width=75, height=32, command=self.paste_selected)
        self.btn_paste.pack(side="left", padx=2, pady=6)

        self.btn_auto_cat = ctk.CTkButton(self.opts_frame, text="Auto Organize", fg_color="#1e293b", hover_color="#334155", width=120, height=32, command=self.auto_categorize)
        self.btn_auto_cat.pack(side="left", padx=2, pady=6)

        self.sort_menu = ctk.CTkOptionMenu(
            self.opts_frame, values=["Size (Largest First)", "Size (Smallest First)", "Name (A-Z)", "File Extension"],
            command=self.handle_sort_change, width=180, height=32
        )
        self.sort_menu.set(self.current_sort)
        self.sort_menu.pack(side="right", padx=(2, 10), pady=6)

        self.btn_select_all = ctk.CTkButton(self.opts_frame, text="Toggle All", width=100, height=32, fg_color="#1e293b", hover_color="#334155", command=self.toggle_all)
        self.btn_select_all.pack(side="right", padx=2, pady=6)

        self.list_title = ctk.CTkLabel(self, text="Target Items (W/S to navigate, Enter/Space to select, D/Right to open folder):", text_color=self.text_muted, anchor="w")
        self.list_title.pack(fill="x", padx=20, pady=(4, 2))

        self.scroll_area = ctk.CTkScrollableFrame(self, height=200, corner_radius=10, fg_color=self.card_bg, border_width=1, border_color=self.panel_border)
        self.scroll_area.pack(fill="both", expand=True, padx=16, pady=4)
        self.scroll_area._parent_canvas.bind("<MouseWheel>", self._on_mousewheel, add="+")

        self.log_view = ctk.CTkTextbox(self, height=95, corner_radius=8, fg_color=self.inner_bg, border_width=1, border_color=self.panel_border, text_color=self.text_main)
        self.log_view.pack(fill="x", padx=16, pady=(3, 6))

        bottom_bar = ctk.CTkFrame(self, fg_color="transparent")
        bottom_bar.pack(fill="x", padx=16, pady=(0, 10))

        self.btn_refresh = ctk.CTkButton(bottom_bar, text="Refresh & Rescan", height=38, command=self.refresh_list)
        self.btn_refresh.pack(side="left", fill="x", expand=True, padx=(0, 6))

        self.btn_delete = ctk.CTkButton(bottom_bar, text="Delete Selected", fg_color="#7f1d1d", hover_color="#991b1b", text_color="#ffffff", height=38, command=self.delete_selected)
        self.btn_delete.pack(side="right", fill="x", expand=True, padx=(6, 0))

    def apply_font(self, font_name):
        self.current_font = font_name
        f = FONT_PROFILES.get(font_name, FONT_PROFILES["Futuristic (Bahnschrift)"])

        self.app_title.configure(font=f["title"])
        self.font_picker.configure(font=f["ui_sm"], dropdown_font=f["ui_sm"])
        self.theme_picker.configure(font=f["ui_sm"], dropdown_font=f["ui_sm"])
        self.btn_mode_toggle.configure(font=f["ui_bold"])
        self.btn_up.configure(font=f["ui_bold"])
        self.lbl_path.configure(font=f["ui_bold"])
        self.entry_path.configure(font=f["mono"])
        self.btn_browse.configure(font=f["ui_bold"])
        self.entry_new_folder.configure(font=f["ui_sm"])
        self.btn_move.configure(font=f["ui_bold"])
        self.btn_cut.configure(font=f["ui_bold"])
        self.btn_paste.configure(font=f["ui_bold"])
        self.btn_auto_cat.configure(font=f["ui_bold"])
        self.sort_menu.configure(font=f["ui_sm"], dropdown_font=f["ui_sm"])
        self.btn_select_all.configure(font=f["ui_bold"])
        self.list_title.configure(font=f["ui_bold"])
        self.log_view.configure(font=f["mono"])
        self.btn_refresh.configure(font=f["ui_bold"])
        self.btn_delete.configure(font=f["ui_bold"])

    def apply_theme(self, theme_name):
        self.current_theme = theme_name
        palette = THEMES.get(theme_name, THEMES["Emerald"])
        pri = palette["primary"]

        self.app_title.configure(text_color=pri)
        self.btn_move.configure(fg_color=palette["btn_bg"], hover_color=palette["btn_hover"], border_color=pri, border_width=1, text_color="#ffffff")
        self.btn_refresh.configure(fg_color=palette["btn_bg"], hover_color=palette["btn_hover"], border_color=pri, border_width=1, text_color="#ffffff")
        
        self.font_picker.configure(fg_color=palette["menu_bg"], button_color=pri, button_hover_color=palette["hover"])
        self.theme_picker.configure(fg_color=palette["menu_bg"], button_color=pri, button_hover_color=palette["hover"])
        self.sort_menu.configure(fg_color=palette["menu_bg"], button_color=pri, button_hover_color=palette["hover"])

        self.btn_auto_cat.configure(hover_color=palette["btn_hover"])
        self.btn_cut.configure(hover_color=palette["btn_hover"])
        self.btn_paste.configure(hover_color=palette["btn_hover"])
        self.btn_select_all.configure(hover_color=palette["btn_hover"])
        self.btn_up.configure(hover_color=palette["btn_hover"])
        self.btn_browse.configure(hover_color=palette["btn_hover"])

    def handle_font_change(self, font_name):
        self.apply_font(font_name)
        self.save_config()
        self._render_scanned_items(self.scanned_items_data)

    def handle_theme_change(self, theme_name):
        if theme_name not in THEMES:
            theme_name = "Emerald"
        self.apply_theme(theme_name)
        self.save_config()
        self._render_scanned_items(self.scanned_items_data)

    def _bind_global_key_events(self):
        self.bind_all("<KeyPress>", self._on_global_key_press)

    def _is_typing(self):
        f = self.focus_get()
        if not f: return False
        return isinstance(f, (tk.Entry, tk.Text)) or "entry" in str(type(f)).lower() or "text" in str(type(f)).lower()

    def _on_global_key_press(self, event):
        if event.state & 4:
            k = event.keysym.lower()
            if k == "x" and not self._is_typing():
                self.cut_selected()
                return "break"
            elif k == "v" and not self._is_typing() and self.cut_clipboard_items:
                self.paste_selected()
                return "break"

        if self._is_typing() or not self.current_display_items:
            return

        now = time.time()
        key = event.keysym.lower()
        char = event.char.lower() if event.char else ""

        is_nav_key = key in ("up", "w", "down", "s") or char in ("w", "ص", "s", "س")
        if is_nav_key:
            if now - self.last_key_time < 0.04:
                return "break"
            self.last_key_time = now

        if key in ("up", "w") or char in ("w", "ص"):
            return self._handle_key_nav("up")
        elif key in ("down", "s") or char in ("s", "س"):
            return self._handle_key_nav("down")
        elif key in ("left", "a", "backspace") or char in ("a", "ش"):
            return self._handle_key_nav("left")
        elif key in ("right", "d") or char in ("d", "ي"):
            return self._handle_key_nav("open")
        elif key in ("return", "kp_enter", "space"):
            return self._handle_key_nav("toggle")

    def _handle_key_nav(self, action):
        if not self.current_display_items:
            return "break"

        old_idx = self.focused_index
        if action == "up":
            if self.focused_index > 0:
                self.focused_index -= 1
                self._update_single_focus(old_idx, self.focused_index)
            return "break"
        elif action == "down":
            if self.focused_index < len(self.current_display_items) - 1:
                self.focused_index += 1
                self._update_single_focus(old_idx, self.focused_index)
            return "break"
        elif action == "left":
            self.navigate_up()
            return "break"
        elif action == "open":
            if 0 <= self.focused_index < len(self.current_display_items):
                item = self.current_display_items[self.focused_index]
                if item[2]:
                    self.open_subfolder(item[0])
            return "break"
        elif action == "toggle":
            if 0 <= self.focused_index < len(self.current_display_items):
                name = self.current_display_items[self.focused_index][0]
                if name in self.file_vars:
                    self.file_vars[name].set(not self.file_vars[name].get())
            return "break"

    def _update_single_focus(self, old_idx, new_idx):
        palette = THEMES.get(self.current_theme, THEMES["Emerald"])
        focus_bg = palette["focus_dark"] if self.appearance_mode == "Dark" else palette["focus_light"]

        if 0 <= old_idx < len(self.row_widgets):
            self.row_widgets[old_idx][0].configure(fg_color="transparent", border_width=0)

        if 0 <= new_idx < len(self.row_widgets):
            self.row_widgets[new_idx][0].configure(fg_color=focus_bg, border_width=1, border_color=palette["focus_border"])

            try:
                canvas = self.scroll_area._parent_canvas
                total = max(1, len(self.row_widgets))
                view_top, view_bottom = canvas.yview()
                view_height = max(0.01, view_bottom - view_top)

                item_top = new_idx / total
                item_bottom = (new_idx + 1) / total
                padding = max(0.02, view_height * 0.22)

                if item_bottom > view_bottom - padding:
                    target = item_bottom - view_height + padding
                    canvas.yview_moveto(min(1.0, max(0.0, target)))
                elif item_top < view_top + padding:
                    target = item_top - padding
                    canvas.yview_moveto(max(0.0, target))
            except Exception:
                pass

    def _on_mousewheel(self, event):
        try:
            self.scroll_area._parent_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        except Exception:
            pass

    def log(self, text):
        self.log_view.insert("end", text + "\n")
        self.log_view.see("end")

    def toggle_appearance(self):
        self.appearance_mode = "Light" if self.appearance_mode == "Dark" else "Dark"
        ctk.set_appearance_mode(self.appearance_mode)
        self.btn_mode_toggle.configure(text="Dark" if self.appearance_mode == "Dark" else "Light")
        self._apply_appearance_backgrounds()

        self.header.configure(fg_color=self.card_bg, border_color=self.panel_border)
        self.dir_frame.configure(fg_color=self.card_bg, border_color=self.panel_border)
        self.opts_frame.configure(fg_color=self.card_bg, border_color=self.panel_border)
        self.scroll_area.configure(fg_color=self.card_bg, border_color=self.panel_border)
        self.entry_path.configure(fg_color=self.inner_bg, border_color=self.panel_border, text_color=self.text_main)
        self.entry_new_folder.configure(fg_color=self.inner_bg, border_color=self.panel_border, text_color=self.text_main)
        self.log_view.configure(fg_color=self.inner_bg, border_color=self.panel_border, text_color=self.text_main)
        self.lbl_path.configure(text_color=self.text_muted)
        self.list_title.configure(text_color=self.text_muted)

        self.apply_theme(self.current_theme)
        self.save_config()
        self._render_scanned_items(self.scanned_items_data)

    def choose_directory(self):
        folder = filedialog.askdirectory(initialdir=self.working_dir)
        if folder:
            self.working_dir = os.path.abspath(folder)
            self.entry_path.delete(0, "end")
            self.entry_path.insert(0, self.working_dir)
            self.save_config()
            self.refresh_list()

    def navigate_up(self):
        parent = os.path.dirname(self.working_dir)
        if parent and os.path.exists(parent) and parent != self.working_dir:
            self.working_dir = os.path.abspath(parent)
            self.entry_path.delete(0, "end")
            self.entry_path.insert(0, self.working_dir)
            self.save_config()
            self.refresh_list()

    def open_subfolder(self, folder_name):
        new_path = os.path.abspath(os.path.join(self.working_dir, folder_name))
        if os.path.isdir(new_path):
            self.working_dir = new_path
            self.entry_path.delete(0, "end")
            self.entry_path.insert(0, self.working_dir)
            self.save_config()
            self.refresh_list()

    def toggle_all(self):
        if not self.file_vars: return
        target = not all(var.get() for var in self.file_vars.values())
        for var in self.file_vars.values():
            var.set(target)

    def handle_sort_change(self, _=None):
        self.displayed_count = 100
        self.save_config()
        self._render_scanned_items(self.scanned_items_data)

    def load_more(self):
        self.displayed_count += 100
        self._render_scanned_items(self.scanned_items_data)

    def refresh_list(self):
        if self.is_scanning: return
        custom_path = self.entry_path.get().strip()
        if os.path.isdir(custom_path):
            self.working_dir = os.path.abspath(custom_path)

        if not os.path.exists(self.working_dir):
            self.log(f"Invalid path: {self.working_dir}")
            return

        self.is_scanning = True
        self.displayed_count = 100
        self.btn_refresh.configure(state="disabled", text="Scanning...")

        for widget in self.scroll_area.winfo_children(): widget.destroy()
        self.file_vars.clear()
        self.row_widgets.clear()
        self.scanned_items_data.clear()

        threading.Thread(target=self._scan_thread_worker, daemon=True).start()

    def _scan_thread_worker(self):
        try:
            try:
                all_items = os.listdir(self.working_dir)
            except Exception as e:
                self.after(0, lambda: self.log(f"Access error: {e}"))
                all_items = []

            targets = [
                f for f in all_items
                if f not in ("config.json", "app_icon.ico")
                and not f.startswith('.')
                and not f.endswith(('.py', '.pyw', '.ico', '.bat'))
            ]

            def process_single_item(name):
                item_path = os.path.join(self.working_dir, name)
                is_dir = os.path.isdir(item_path)
                size_bytes = calculate_size_ultra_fast(item_path)
                if size_bytes < 1024:
                    return None
                ext = os.path.splitext(name)[1].lower() if not is_dir else "folder"
                return (name, size_bytes, is_dir, ext)

            with ThreadPoolExecutor(max_workers=8) as executor:
                results = list(executor.map(process_single_item, targets))

            processed = [item for item in results if item is not None]
            self.scanned_items_data = processed
            self.after(0, lambda: self._render_scanned_items(processed))
        except Exception as e:
            self.after(0, lambda: self.log(f"Scan failed: {e}"))
            self.after(0, lambda: self._render_scanned_items([]))
        finally:
            self.is_scanning = False
            self.after(0, lambda: self.btn_refresh.configure(state="normal", text="Refresh & Rescan"))

    def _render_scanned_items(self, raw_items):
        for widget in self.scroll_area.winfo_children(): widget.destroy()
        self.file_vars.clear()
        self.row_widgets.clear()
        self.focused_index = 0

        f = FONT_PROFILES.get(self.current_font, FONT_PROFILES["Futuristic (Bahnschrift)"])
        if not raw_items:
            lbl = ctk.CTkLabel(self.scroll_area, text="No items found (or all items < 1KB).", font=f["ui_bold"], text_color=self.text_muted)
            lbl.pack(pady=25)
            self.current_display_items = []
        else:
            sort_choice = self.sort_menu.get()
            if sort_choice == "Size (Largest First)":
                sorted_items = sorted(raw_items, key=lambda x: x[1], reverse=True)
            elif sort_choice == "Size (Smallest First)":
                sorted_items = sorted(raw_items, key=lambda x: x[1])
            elif sort_choice == "Name (A-Z)":
                sorted_items = sorted(raw_items, key=lambda x: x[0].lower())
            else:
                sorted_items = sorted(raw_items, key=lambda x: (not x[2], x[3], x[0].lower()))

            self.current_display_items = sorted_items[:self.displayed_count]
            palette = THEMES.get(self.current_theme, THEMES["Emerald"])
            total_dir_size = sum(item[1] for item in sorted_items)

            badge_bg = palette["badge_dark"] if self.appearance_mode == "Dark" else palette["badge_light"]
            badge_fg = palette["badge_text_dark"] if self.appearance_mode == "Dark" else palette["badge_text_light"]

            for idx, (name, size_bytes, is_dir, _) in enumerate(self.current_display_items):
                icon_tag = "📁" if is_dir else "📄"
                size_str = format_size(size_bytes)
                var = ctk.BooleanVar(value=False)

                row_frame = ctk.CTkFrame(self.scroll_area, fg_color="transparent", corner_radius=8)
                row_frame.pack(fill="x", padx=4, pady=2)

                left_box = ctk.CTkFrame(row_frame, fg_color="transparent")
                left_box.pack(side="left", fill="x", expand=True, padx=4, pady=3)

                chk = ctk.CTkCheckBox(
                    left_box, text="", variable=var, width=20,
                    fg_color=palette["primary"], hover_color=palette["hover"]
                )
                chk.pack(side="left", padx=(4, 6))

                lbl_icon = ctk.CTkLabel(left_box, text=icon_tag, font=("Segoe UI Emoji", 12))
                lbl_icon.pack(side="left", padx=(0, 6))

                display_name = name if len(name) <= 45 else name[:42] + "..."
                lbl_name = ctk.CTkLabel(
                    left_box, text=display_name, font=f["row_main"],
                    text_color=self.text_main, anchor="w"
                )
                lbl_name.pack(side="left", fill="x", expand=True)

                right_box = ctk.CTkFrame(row_frame, fg_color="transparent")
                right_box.pack(side="right", padx=6, pady=3)

                lbl_size = ctk.CTkLabel(
                    right_box, text=f" {size_str} ", font=f["badge"],
                    fg_color=badge_bg, text_color=badge_fg, corner_radius=6, height=24
                )
                lbl_size.pack(side="left", padx=4)

                btn_open = None
                if is_dir:
                    btn_open = ctk.CTkButton(
                        right_box, text="Open", width=60, height=24,
                        font=f["ui_sm"], fg_color="#1e293b", hover_color=palette["hover"],
                        command=lambda n=name: self.open_subfolder(n)
                    )
                    btn_open.pack(side="left", padx=4)

                    row_frame.bind("<Double-Button-1>", lambda e, n=name: self.open_subfolder(n))
                    lbl_name.bind("<Double-Button-1>", lambda e, n=name: self.open_subfolder(n))

                self.file_vars[name] = var
                self.row_widgets.append((row_frame, chk, btn_open))

            if len(sorted_items) > self.displayed_count:
                btn_more = ctk.CTkButton(
                    self.scroll_area, text=f"Show More ({len(sorted_items) - self.displayed_count} Remaining)",
                    font=f["ui_bold"], fg_color="#1e293b", hover_color=palette["hover"],
                    command=self.load_more, height=32
                )
                btn_more.pack(fill="x", padx=20, pady=8)

            if self.row_widgets:
                self._update_single_focus(0, 0)

            self.log(f"Showing top {len(self.current_display_items)} of {len(sorted_items)} items. Total: {format_size(total_dir_size)}")

    def cut_selected(self):
        selected = [name for name, var in self.file_vars.items() if var.get()]
        if not selected:
            messagebox.showwarning("Warning", "No items selected to cut.")
            return
        self.cut_clipboard_items = [os.path.join(self.working_dir, name) for name in selected]
        self.log(f"Cut {len(self.cut_clipboard_items)} item(s) to clipboard.")

    def paste_selected(self):
        if not self.cut_clipboard_items:
            messagebox.showinfo("Info", "Clipboard is empty.")
            return
        moved = 0
        for src in self.cut_clipboard_items:
            if not os.path.exists(src): continue
            name = os.path.basename(src)
            dst = os.path.join(self.working_dir, name)
            try:
                if src != dst:
                    shutil.move(src, dst)
                    moved += 1
            except Exception as e:
                self.log(f"Error moving {name}: {e}")
        self.cut_clipboard_items.clear()
        self.log(f"Pasted {moved} item(s) successfully.")
        self.refresh_list()

    def move_selected(self):
        dest_folder = self.entry_new_folder.get().strip()
        selected = [name for name, var in self.file_vars.items() if var.get()]
        if not dest_folder:
            messagebox.showwarning("Warning", "Please provide a target folder name.")
            return
        if not selected:
            messagebox.showwarning("Warning", "No items selected.")
            return

        target_path = os.path.join(self.working_dir, dest_folder)
        os.makedirs(target_path, exist_ok=True)
        moved = 0
        for name in selected:
            src = os.path.join(self.working_dir, name)
            dst = os.path.join(target_path, name)
            try:
                if src != target_path:
                    shutil.move(src, dst)
                    moved += 1
            except Exception as e:
                self.log(f"Error moving {name}: {e}")
        self.log(f"Moved {moved} item(s) into '{dest_folder}'.")
        self.entry_new_folder.delete(0, "end")
        self.refresh_list()

    def auto_categorize(self):
        raw_items = [item for item in self.scanned_items_data if not item[2]]
        if not raw_items:
            messagebox.showinfo("Info", "No files found to categorize.")
            return
        if not messagebox.askyesno("Confirm", f"Automatically sort {len(raw_items)} files into folders?"):
            return

        sorted_count = 0
        for name, _, _, ext in raw_items:
            target_cat = "Miscellaneous"
            for cat_name, exts in CATEGORY_RULES.items():
                if ext in exts:
                    target_cat = cat_name
                    break
            cat_dir = os.path.join(self.working_dir, target_cat)
            os.makedirs(cat_dir, exist_ok=True)
            src = os.path.join(self.working_dir, name)
            dst = os.path.join(cat_dir, name)
            try:
                shutil.move(src, dst)
                sorted_count += 1
            except Exception as e:
                self.log(f"Error: {e}")
        self.log(f"Auto-categorized {sorted_count} files.")
        self.refresh_list()

    def delete_selected(self):
        selected = [name for name, var in self.file_vars.items() if var.get()]
        if not selected:
            messagebox.showwarning("Warning", "No items selected.")
            return
        if not messagebox.askyesno("Confirm Delete", f"Permanently delete {len(selected)} item(s)?"):
            return

        for name in selected:
            p = os.path.join(self.working_dir, name)
            try:
                shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
                self.log(f"Deleted: {name}")
            except Exception as e:
                self.log(f"Failed to delete {name}: {e}")
        self.refresh_list()

if __name__ == "__main__":
    app = StorageManagerApp()
    app.mainloop()