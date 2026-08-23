import os
import sys
import subprocess
import json
import shutil
import threading
import time
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
    root.title("Matrix Engine // Dependency Resolver")
    root.geometry("500x300")
    root.resizable(False, False)
    root.configure(bg="#080b0e")

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    root.geometry(f"500x300+{int((ws-500)/2)}+{int((hs-300)/2)}")

    tk.Label(root, text="[!] MISSING SYSTEM DEPENDENCIES", font=("Consolas", 13, "bold"), fg="#ff3355", bg="#080b0e").pack(pady=(20, 8))
    tk.Label(root, text="The following required Python packages were not located:", font=("Segoe UI", 10), fg="#94a3b8", bg="#080b0e").pack()

    list_frame = tk.Frame(root, bg="#0e161c", bd=1, relief="solid")
    list_frame.pack(fill="x", padx=30, pady=12)
    for pkg in missing:
        tk.Label(list_frame, text=f"• {pkg}", font=("Consolas", 11, "bold"), fg="#00ff66", bg="#0e161c").pack(anchor="w", padx=15, pady=3)

    def install_and_restart():
        root.destroy()
        py_exe = sys.executable
        if py_exe.lower().endswith("pythonw.exe"):
            py_exe = py_exe[:-10] + "python.exe"

        script_path = os.path.abspath(__file__)
        bat_cmd = f"""@echo off
title Installing Dependencies...
echo [*] Installing missing packages: {" ".join(missing)}
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

    btn_frame = tk.Frame(root, bg="#080b0e")
    btn_frame.pack(fill="x", padx=30, pady=(10, 15))
    tk.Button(btn_frame, text="EXIT", font=("Segoe UI", 10, "bold"), bg="#1e293b", fg="#ffffff", bd=0, padx=15, pady=6, command=sys.exit).pack(side="left")
    tk.Button(btn_frame, text="[► INSTALL DEPENDENCIES & LAUNCH]", font=("Segoe UI", 10, "bold"), bg="#005a24", fg="#00ff66", bd=0, padx=15, pady=6, command=install_and_restart).pack(side="right")

    root.mainloop()
    sys.exit()

from PIL import Image
import customtkinter as ctk

SCRIPT_FILE = os.path.abspath(__file__)
SCRIPT_DIR = os.path.dirname(SCRIPT_FILE)
CONFIG_FILE = os.path.join(SCRIPT_DIR, "config.json")
APP_ICON_FILE = os.path.join(SCRIPT_DIR, "app_icon.ico")

IMAGE_EXTS = (('Image Files', '*.png;*.jpg;*.jpeg;*.webp;*.bmp;*.ico'), ('All Files', '*.*'))

CATEGORY_RULES = {
    "Images": ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.svg', '.ico', '.tiff'],
    "Documents": ['.pdf', '.docx', '.doc', '.xlsx', '.xls', '.pptx', '.ppt', '.txt', '.csv', '.rtf', '.md'],
    "Media_Videos": ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm'],
    "Media_Audio": ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma'],
    "Archives": ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.iso'],
    "Executables": ['.exe', '.msi', '.bat', '.cmd', '.apk', '.jar'],
    "Developer_Code": ['.py', '.pyw', '.js', '.html', '.css', '.cpp', '.c', '.cs', '.java', '.json', '.xml', '.sql', '.php', '.ts']
}

FONT_PROFILES = {
    "Retro Matrix (Consolas)": {
        "title": ("Consolas", 15, "bold"), "ui_bold": ("Consolas", 11, "bold"),
        "ui_sm": ("Consolas", 10, "bold"), "file": ("Consolas", 11, "bold"), "console": ("Consolas", 10, "bold")
    },
    "Modern Bold (Segoe UI)": {
        "title": ("Segoe UI", 15, "bold"), "ui_bold": ("Segoe UI", 11, "bold"),
        "ui_sm": ("Segoe UI", 10, "bold"), "file": ("Segoe UI", 11, "bold"), "console": ("Consolas", 10, "bold")
    },
    "Cyber Terminal (Lucida Console)": {
        "title": ("Lucida Console", 14, "bold"), "ui_bold": ("Lucida Console", 10, "bold"),
        "ui_sm": ("Lucida Console", 9, "bold"), "file": ("Lucida Console", 10, "bold"), "console": ("Lucida Console", 10, "bold")
    },
    "Developer Mono (Cascadia Mono)": {
        "title": ("Cascadia Mono", 14, "bold"), "ui_bold": ("Cascadia Mono", 10, "bold"),
        "ui_sm": ("Cascadia Mono", 9, "bold"), "file": ("Cascadia Mono", 10, "bold"), "console": ("Cascadia Mono", 10, "bold")
    }
}

THEME_PALETTES = {
    "Green": {"primary": "#00ff66", "hover": "#00cc52", "border": "#10b981", "dark_bg": "#005a24", "dark_hover": "#008033", "focus": "#064e3b"},
    "Red": {"primary": "#ff3355", "hover": "#e61e3f", "border": "#f43f5e", "dark_bg": "#7f1d1d", "dark_hover": "#991b1b", "focus": "#450a0a"},
    "Blue": {"primary": "#38bdf8", "hover": "#0ea5e9", "border": "#0284c7", "dark_bg": "#0369a1", "dark_hover": "#0284c7", "focus": "#082f49"},
    "Yellow": {"primary": "#facc15", "hover": "#eab308", "border": "#ca8a04", "dark_bg": "#854d0e", "dark_hover": "#a16207", "focus": "#422006"},
    "Purple": {"primary": "#c084fc", "hover": "#a855f7", "border": "#9333ea", "dark_bg": "#581c87", "dark_hover": "#6b21a8", "focus": "#3b0764"},
    "Turquoise": {"primary": "#2dd4bf", "hover": "#14b8a6", "border": "#0d9488", "dark_bg": "#115e59", "dark_hover": "#0f766e", "focus": "#042f2e"}
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

def process_and_save_ico(input_image_path, output_ico_path):
    try:
        img = Image.open(input_image_path).convert("RGBA")
        width, height = img.size
        min_dim = min(width, height)
        left = (width - min_dim) // 2
        top = (height - min_dim) // 2
        cropped_img = img.crop((left, top, left + min_dim, top + min_dim))
        sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
        cropped_img.save(output_ico_path, format="ICO", sizes=sizes)
        return True
    except Exception:
        return False

def make_desktop_shortcut(target, link_path, icon_path=None):
    try:
        working_dir = os.path.dirname(target)
        icon_line = f'oLink.IconLocation = "{icon_path}"' if (icon_path and os.path.exists(icon_path)) else ""
        vbs_script = f'''
        Set oWS = WScript.CreateObject("WScript.Shell")
        sLinkFile = "{link_path}"
        Set oLink = oWS.CreateShortcut(sLinkFile)
        oLink.TargetPath = "{target}"
        oLink.WorkingDirectory = "{working_dir}"
        oLink.Description = "Matrix Storage Engine"
        {icon_line}
        oLink.Save
        '''
        vbs_path = os.path.join(os.environ.get("TEMP", os.path.expanduser("~")), "_make_shortcut.vbs")
        with open(vbs_path, "w", encoding="utf-8") as f:
            f.write(vbs_script)
            
        subprocess.run(["wscript", vbs_path], creationflags=0x08000000 if sys.platform == "win32" else 0)
        if os.path.exists(vbs_path):
            os.remove(vbs_path)
            
        return os.path.exists(link_path)
    except Exception:
        return False

class HotCodeUpdaterModal(ctk.CTkToplevel):
    def __init__(self, parent, target_file, restart_callback, theme_color="Green", appearance_mode="Dark"):
        super().__init__(parent)
        self.title("Matrix Hot-Code Engine Overhaul")
        self.geometry("820x580")
        self.target_file = target_file
        self.restart_callback = restart_callback
        self.palette = THEME_PALETTES.get(theme_color, THEME_PALETTES["Green"])
        
        bg_color = "#080b0e" if appearance_mode == "Dark" else "#e2e8f0"
        self.configure(fg_color=bg_color)
        self.transient(parent)
        self.grab_set()

        pri = self.palette["primary"]
        txt_main = "#ffffff" if appearance_mode == "Dark" else "#0f172a"
        inner_bg = "#050709" if appearance_mode == "Dark" else "#f1f5f9"

        header_box = ctk.CTkFrame(self, fg_color="transparent")
        header_box.pack(fill="x", padx=16, pady=(12, 6))

        lbl = ctk.CTkLabel(header_box, text="[❖] CODE PAYLOAD INJECTION / EXPORT:", font=("Consolas", 12, "bold"), text_color=pri)
        lbl.pack(side="left")

        actions_box = ctk.CTkFrame(header_box, fg_color="transparent")
        actions_box.pack(side="right")

        ctk.CTkButton(actions_box, text="📋 COPY CODE", width=110, height=28, font=("Segoe UI", 11, "bold"), fg_color="#1e293b", hover_color="#334155", text_color="#ffffff", command=self.copy_current_code).pack(side="left", padx=(0, 6))
        ctk.CTkButton(actions_box, text="📥 PASTE CODE", width=110, height=28, font=("Segoe UI", 11, "bold"), fg_color=self.palette["dark_bg"], hover_color=self.palette["hover"], text_color=pri if appearance_mode == "Dark" else "#ffffff", command=self.paste_from_clipboard).pack(side="left")

        self.txt_code = ctk.CTkTextbox(self, font=("Consolas", 11), fg_color=inner_bg, border_color=pri, border_width=1, text_color=txt_main, undo=True)
        self.txt_code.pack(fill="both", expand=True, padx=16, pady=6)

        try:
            with open(self.target_file, "r", encoding="utf-8") as f:
                self.txt_code.insert("1.0", f.read())
        except Exception: pass

        btn_box = ctk.CTkFrame(self, fg_color="transparent")
        btn_box.pack(fill="x", padx=16, pady=(0, 14))

        ctk.CTkButton(btn_box, text="CANCEL", width=100, font=("Segoe UI", 11, "bold"), fg_color="#1e293b", command=self.destroy).pack(side="left")
        ctk.CTkButton(btn_box, text="[► INJECT CODE & RESTART INSTANCE]", font=("Segoe UI", 11, "bold"), fg_color=self.palette["dark_bg"], hover_color=self.palette["dark_hover"], border_width=1, border_color=pri, text_color=pri if appearance_mode == "Dark" else "#ffffff", command=self.apply_update).pack(side="right", fill="x", expand=True, padx=(10, 0))

    def copy_current_code(self):
        try:
            with open(self.target_file, "r", encoding="utf-8") as f:
                code_data = f.read()
            self.clipboard_clear()
            self.clipboard_append(code_data)
            self.update()
            messagebox.showinfo("Clipboard", "Complete application code copied to clipboard!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read source: {e}")

    def paste_from_clipboard(self):
        try:
            clipboard_text = self.clipboard_get()
            if clipboard_text:
                self.txt_code.delete("1.0", "end")
                self.txt_code.insert("1.0", clipboard_text)
        except Exception as e:
            messagebox.showwarning("Clipboard Warning", f"Could not access clipboard: {e}")

    def apply_update(self):
        code = self.txt_code.get("1.0", "end-1c").strip()
        if len(code) < 50 or "import" not in code:
            messagebox.showerror("Payload Error", "Invalid script payload provided.")
            return

        try:
            with open(self.target_file, 'w', encoding='utf-8') as f:
                f.write(code)
            messagebox.showinfo("Success", "Engine updated successfully! Restarting instance...")
            self.destroy()
            self.restart_callback()
        except Exception as e:
            messagebox.showerror("Write Error", f"Failed to rewrite source: {str(e)}")

class MatrixStorageManager(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MATRIX // STORAGE_MANAGER_SUITE_V6.0")
        self.minsize(920, 620)

        self.config = self.load_config()

        if os.path.exists(APP_ICON_FILE):
            try: self.iconbitmap(APP_ICON_FILE)
            except Exception: pass

        saved_geometry = self.config.get("window_geometry", "980x680")
        try: self.geometry(saved_geometry)
        except Exception: self.geometry("980x680")

        if self.config.get("is_maximized", False):
            self.after(100, lambda: self.state("zoomed"))

        self.current_font_profile = self.config.get("font_profile", "Retro Matrix (Consolas)")
        self.current_theme_color = self.config.get("theme_color", "Green")
        self.current_appearance = self.config.get("appearance_mode", "Dark")
        self.target_dir = self.config.get("target_dir", SCRIPT_DIR)
        self.current_sort = self.config.get("sort_mode", "Size (Largest First)")

        if not os.path.exists(self.target_dir):
            self.target_dir = SCRIPT_DIR

        ctk.set_appearance_mode(self.current_appearance)

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
        self._build_matrix_ui()
        self.apply_theme(self.current_theme_color)
        self.apply_font_profile(self.current_font_profile)
        self._bind_global_key_events()

        self.protocol("WM_DELETE_WINDOW", self.on_app_close)
        self.refresh_file_list()

    def load_config(self):
        default_cfg = {
            "window_geometry": "980x680", "is_maximized": False,
            "font_profile": "Retro Matrix (Consolas)", "theme_color": "Green",
            "appearance_mode": "Dark", "target_dir": SCRIPT_DIR,
            "sort_mode": "Size (Largest First)"
        }
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                    default_cfg.update(json.load(f))
            except Exception: pass
        return default_cfg

    def save_config(self):
        try:
            is_max = (self.state() == "zoomed")
            current_geom = self.config.get("window_geometry", "980x680") if is_max else self.geometry()

            self.config = {
                "window_geometry": current_geom, "is_maximized": is_max,
                "font_profile": self.current_font_profile, "theme_color": self.current_theme_color,
                "appearance_mode": self.current_appearance, "target_dir": self.target_dir,
                "sort_mode": self.sort_menu.get()
            }
            with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=4)
        except Exception: pass

    def on_app_close(self):
        self.save_config()
        self.destroy()

    def restart_application(self):
        self.save_config()
        subprocess.Popen([sys.executable.replace("python.exe", "pythonw.exe"), SCRIPT_FILE], creationflags=0x08000000 if sys.platform == "win32" else 0)
        self.destroy()
        sys.exit()

    def open_hot_updater(self):
        HotCodeUpdaterModal(self, SCRIPT_FILE, self.restart_application, self.current_theme_color, self.current_appearance)

    def create_desktop_shortcut_now(self):
        desktop_dir = ""
        try:
            import winreg
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders")
            desktop_dir, _ = winreg.QueryValueEx(key, "Desktop")
            desktop_dir = os.path.expandvars(desktop_dir)
        except Exception:
            desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")

        desktop_lnk = os.path.join(desktop_dir, "Matrix Storage Manager.lnk")
        icon_arg = APP_ICON_FILE if os.path.exists(APP_ICON_FILE) else None
        
        if make_desktop_shortcut(SCRIPT_FILE, desktop_lnk, icon_path=icon_arg):
            messagebox.showinfo("Success", f"[❖] DESKTOP PAYLOAD LINK GENERATED:\n{desktop_lnk}")
        else:
            messagebox.showerror("Error", "[!] Failed to establish desktop shortcut link.")

    def change_app_icon_live(self):
        img_p = filedialog.askopenfilename(title="Select New Icon / Image File", filetypes=IMAGE_EXTS)
        if img_p:
            if process_and_save_ico(img_p, APP_ICON_FILE):
                try:
                    self.iconbitmap(APP_ICON_FILE)
                    messagebox.showinfo("Icon Updated", "App icon generated and applied successfully!")
                except Exception as e:
                    messagebox.showwarning("Warning", f"Icon saved, restart app to fully reflect: {e}")

    def _apply_appearance_backgrounds(self):
        if self.current_appearance == "Dark":
            self.configure(fg_color="#080b0e")
            self.card_bg = "#0d1318"
            self.inner_bg = "#050709"
            self.panel_border = "#1e2d38"
            self.text_main = "#ffffff"
            self.text_muted = "#94a3b8"
        else:
            self.configure(fg_color="#e2e8f0")
            self.card_bg = "#cbd5e1"
            self.inner_bg = "#f1f5f9"
            self.panel_border = "#94a3b8"
            self.text_main = "#0f172a"
            self.text_muted = "#334155"

    def _build_matrix_ui(self):
        f = FONT_PROFILES.get(self.current_font_profile, FONT_PROFILES["Retro Matrix (Consolas)"])

        self.header_frame = ctk.CTkFrame(self, fg_color=self.card_bg, corner_radius=10, border_width=1, border_color=self.panel_border)
        self.header_frame.pack(fill="x", padx=14, pady=(10, 4))

        top_bar = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        top_bar.pack(fill="x", padx=10, pady=(6, 6))

        self.title_lbl = ctk.CTkLabel(top_bar, text="[❖] MATRIX STORAGE MANAGER", font=f["title"], text_color="#00ff66")
        self.title_lbl.pack(side="left", padx=4, pady=2)

        ctrl_top_box = ctk.CTkFrame(top_bar, fg_color="transparent")
        ctrl_top_box.pack(side="right", padx=2, pady=2)

        self.btn_shortcut = ctk.CTkButton(ctrl_top_box, text="📌 SHORTCUT", width=90, font=f["ui_sm"], fg_color="#1e293b", hover_color="#334155", command=self.create_desktop_shortcut_now)
        self.btn_shortcut.pack(side="left", padx=2)

        self.btn_change_icon = ctk.CTkButton(ctrl_top_box, text="🖼️ ICON", width=65, font=f["ui_sm"], fg_color="#581c87", hover_color="#6b21a8", command=self.change_app_icon_live)
        self.btn_change_icon.pack(side="left", padx=2)

        self.btn_update = ctk.CTkButton(ctrl_top_box, text="⚡ UPDATE", width=75, font=f["ui_sm"], fg_color="#0369a1", hover_color="#0284c7", command=self.open_hot_updater)
        self.btn_update.pack(side="left", padx=2)

        self.font_menu = ctk.CTkOptionMenu(ctrl_top_box, values=list(FONT_PROFILES.keys()), command=self.on_font_selected, width=145, font=f["ui_sm"], dropdown_font=f["ui_sm"])
        self.font_menu.set(self.current_font_profile)
        self.font_menu.pack(side="left", padx=2)

        self.theme_menu = ctk.CTkOptionMenu(ctrl_top_box, values=list(THEME_PALETTES.keys()), command=self.on_theme_selected, width=95, font=f["ui_sm"], dropdown_font=f["ui_sm"])
        self.theme_menu.set(self.current_theme_color)
        self.theme_menu.pack(side="left", padx=2)

        self.btn_toggle_mode = ctk.CTkButton(ctrl_top_box, text="🌙 DARK" if self.current_appearance == "Dark" else "☀️ LIGHT", width=75, font=f["ui_sm"], fg_color="#1e293b", hover_color="#334155", command=self.toggle_appearance_mode)
        self.btn_toggle_mode.pack(side="left", padx=2)

        self.dir_frame = ctk.CTkFrame(self, fg_color=self.card_bg, corner_radius=8, border_width=1, border_color=self.panel_border)
        self.dir_frame.pack(fill="x", padx=14, pady=3)

        self.btn_go_up = ctk.CTkButton(self.dir_frame, text="[⬆ UP]", width=65, font=f["ui_bold"], fg_color="#1e293b", hover_color="#334155", command=self.navigate_up)
        self.btn_go_up.pack(side="left", padx=(10, 4), pady=6)

        self.dir_lbl = ctk.CTkLabel(self.dir_frame, text="PATH:", font=f["ui_bold"], text_color=self.text_muted)
        self.dir_lbl.pack(side="left", padx=(4, 6), pady=6)

        self.dir_entry = ctk.CTkEntry(self.dir_frame, font=f["console"], fg_color=self.inner_bg, border_color=self.panel_border, text_color=self.text_main, height=30)
        self.dir_entry.insert(0, self.target_dir)
        self.dir_entry.pack(side="left", fill="x", expand=True, padx=4, pady=6)
        self.dir_entry.bind("<Return>", lambda _: self.refresh_file_list())

        self.btn_browse = ctk.CTkButton(self.dir_frame, text="[📁 BROWSE]", width=100, font=f["ui_bold"], fg_color="#1e293b", hover_color="#334155", command=self.browse_directory, height=30)
        self.btn_browse.pack(side="right", padx=(4, 10), pady=6)

        self.opts_frame = ctk.CTkFrame(self, fg_color=self.card_bg, corner_radius=8, border_width=1, border_color=self.panel_border)
        self.opts_frame.pack(fill="x", padx=14, pady=3)

        self.new_folder_entry = ctk.CTkEntry(self.opts_frame, placeholder_text="New folder name...", font=f["ui_sm"], fg_color=self.inner_bg, height=30, width=180)
        self.new_folder_entry.pack(side="left", padx=(10, 3), pady=6)

        self.btn_move_selected = ctk.CTkButton(self.opts_frame, text="[➔ MOVE]", font=f["ui_bold"], command=self.move_selected_to_folder, height=30, width=80)
        self.btn_move_selected.pack(side="left", padx=2, pady=6)

        self.btn_cut = ctk.CTkButton(self.opts_frame, text="[✂ CUT]", font=f["ui_bold"], fg_color="#334155", hover_color="#475569", command=self.cut_selected_items, height=30, width=75)
        self.btn_cut.pack(side="left", padx=2, pady=6)

        self.btn_paste = ctk.CTkButton(self.opts_frame, text="[📋 PASTE]", font=f["ui_bold"], fg_color="#1e293b", hover_color="#334155", command=self.paste_cut_items, height=30, width=85)
        self.btn_paste.pack(side="left", padx=2, pady=6)

        self.btn_auto_categorize = ctk.CTkButton(self.opts_frame, text="[⚡ AUTO SORT]", font=f["ui_bold"], fg_color="#334155", hover_color="#475569", command=self.auto_categorize_files, height=30, width=110)
        self.btn_auto_categorize.pack(side="left", padx=2, pady=6)

        self.sort_menu = ctk.CTkOptionMenu(
            self.opts_frame, 
            values=["Size (Largest First)", "Size (Smallest First)", "Name (A-Z)", "File Extension"], 
            command=self.on_sort_changed, 
            width=165, 
            font=f["ui_sm"], 
            dropdown_font=f["ui_sm"],
            height=30
        )
        self.sort_menu.set(self.current_sort)
        self.sort_menu.pack(side="right", padx=(2, 10), pady=6)

        self.btn_select_all = ctk.CTkButton(self.opts_frame, text="TOGGLE ALL", width=95, font=f["ui_bold"], command=self.toggle_all_selection, fg_color="#1e293b", hover_color="#334155", border_width=1, border_color=self.panel_border, height=30)
        self.btn_select_all.pack(side="right", padx=2, pady=6)

        self.list_lbl = ctk.CTkLabel(self, text=">>> DETECTED STORAGE PAYLOADS (W/S to move | Enter/Space to select | D / -> to open folder):", anchor="w", font=f["ui_bold"], text_color=self.text_muted)
        self.list_lbl.pack(fill="x", padx=18, pady=(4, 2))

        self.scroll_frame = ctk.CTkScrollableFrame(self, height=190, corner_radius=8, fg_color=self.card_bg, border_width=1, border_color=self.panel_border)
        self.scroll_frame.pack(fill="both", expand=True, padx=14, pady=3)
        self.scroll_frame._parent_canvas.bind("<MouseWheel>", self._on_mousewheel, add="+")

        console_lbl = ctk.CTkLabel(self, text=">>> SYSTEM ACTIVITY LOG:", anchor="w", font=f["ui_bold"], text_color=self.text_muted)
        console_lbl.pack(fill="x", padx=18, pady=(3, 2))

        self.console = ctk.CTkTextbox(self, height=105, font=f["console"], corner_radius=8, fg_color=self.inner_bg, border_width=1, border_color=self.panel_border, text_color=self.text_main)
        self.console.pack(fill="both", padx=14, pady=(0, 6))

        self.console.tag_config("primary", foreground="#00ff66")
        self.console.tag_config("cyan", foreground="#00f0ff")
        self.console.tag_config("crimson", foreground="#ff3366")
        self.console.tag_config("gold", foreground="#facc15")
        self.console.tag_config("ghost", foreground="#94a3b8")

        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(fill="x", padx=14, pady=(0, 10))

        self.btn_refresh = ctk.CTkButton(btn_frame, text="[⟳ SCAN & ANALYZE DIRECTORY]", font=f["ui_bold"], fg_color="#0f172a" if self.current_appearance == "Dark" else "#475569", hover_color="#1e293b" if self.current_appearance == "Dark" else "#334155", border_width=1, border_color=self.panel_border, text_color="#ffffff", command=self.refresh_file_list, height=38)
        self.btn_refresh.pack(side="left", fill="x", expand=True, padx=(0, 6))

        self.btn_delete_selected = ctk.CTkButton(btn_frame, text="[✖ DELETE SELECTED ITEMS]", font=f["ui_bold"], fg_color="#7f1d1d", hover_color="#991b1b", text_color="#ffffff", command=self.delete_selected_items, height=38)
        self.btn_delete_selected.pack(side="right", fill="x", expand=True, padx=(6, 0))

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
                self.cut_selected_items()
                return "break"
            elif k == "v" and not self._is_typing() and self.cut_clipboard_items:
                self.paste_cut_items()
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
        palette = THEME_PALETTES[self.current_theme_color]
        focus_bg = palette["focus"] if self.current_appearance == "Dark" else "#cbd5e1"

        if 0 <= old_idx < len(self.row_widgets):
            self.row_widgets[old_idx][0].configure(fg_color="transparent", border_width=0)
        
        if 0 <= new_idx < len(self.row_widgets):
            self.row_widgets[new_idx][0].configure(fg_color=focus_bg, border_width=1, border_color=palette["primary"])
            
            try:
                canvas = self.scroll_frame._parent_canvas
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
            self.scroll_frame._parent_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        except Exception:
            pass

    def on_font_selected(self, font_name):
        self.apply_font_profile(font_name)
        self.save_config()

    def on_theme_selected(self, theme_name):
        self.apply_theme(theme_name)
        self.save_config()

    def apply_font_profile(self, profile_name):
        self.current_font_profile = profile_name
        f = FONT_PROFILES.get(profile_name, FONT_PROFILES["Retro Matrix (Consolas)"])

        self.title_lbl.configure(font=f["title"])
        self.btn_shortcut.configure(font=f["ui_sm"])
        self.btn_update.configure(font=f["ui_sm"])
        self.btn_change_icon.configure(font=f["ui_sm"])
        self.font_menu.configure(font=f["ui_sm"], dropdown_font=f["ui_sm"])
        self.theme_menu.configure(font=f["ui_sm"], dropdown_font=f["ui_sm"])
        self.btn_toggle_mode.configure(font=f["ui_sm"])
        self.btn_go_up.configure(font=f["ui_bold"])
        self.dir_lbl.configure(font=f["ui_bold"])
        self.dir_entry.configure(font=f["console"])
        self.btn_browse.configure(font=f["ui_bold"])
        self.new_folder_entry.configure(font=f["ui_sm"])
        self.btn_move_selected.configure(font=f["ui_bold"])
        self.btn_cut.configure(font=f["ui_bold"])
        self.btn_paste.configure(font=f["ui_bold"])
        self.btn_auto_categorize.configure(font=f["ui_bold"])
        self.btn_select_all.configure(font=f["ui_bold"])
        self.sort_menu.configure(font=f["ui_sm"], dropdown_font=f["ui_sm"])
        self.list_lbl.configure(font=f["ui_bold"])
        self.console.configure(font=f["console"])
        self.btn_refresh.configure(font=f["ui_bold"])
        self.btn_delete_selected.configure(font=f["ui_bold"])

        self._render_file_list(self.scanned_items_data)

    def toggle_appearance_mode(self):
        if self.current_appearance == "Dark":
            self.current_appearance = "Light"
            ctk.set_appearance_mode("Light")
            self.btn_toggle_mode.configure(text="☀️ LIGHT")
        else:
            self.current_appearance = "Dark"
            ctk.set_appearance_mode("Dark")
            self.btn_toggle_mode.configure(text="🌙 DARK")

        self._apply_appearance_backgrounds()
        self.header_frame.configure(fg_color=self.card_bg, border_color=self.panel_border)
        self.dir_frame.configure(fg_color=self.card_bg, border_color=self.panel_border)
        self.opts_frame.configure(fg_color=self.card_bg, border_color=self.panel_border)
        self.scroll_frame.configure(fg_color=self.card_bg, border_color=self.panel_border)
        self.dir_entry.configure(fg_color=self.inner_bg, border_color=self.panel_border, text_color=self.text_main)
        self.new_folder_entry.configure(fg_color=self.inner_bg, text_color=self.text_main)
        self.console.configure(fg_color=self.inner_bg, border_color=self.panel_border, text_color=self.text_main)
        self.list_lbl.configure(text_color=self.text_muted)
        self.dir_lbl.configure(text_color=self.text_muted)
        self.btn_refresh.configure(fg_color="#0f172a" if self.current_appearance == "Dark" else "#475569", hover_color="#1e293b" if self.current_appearance == "Dark" else "#334155", border_color=self.panel_border)

        self.apply_theme(self.current_theme_color)
        self.save_config()
        self._render_file_list(self.scanned_items_data)

    def apply_theme(self, theme_name):
        self.current_theme_color = theme_name
        palette = THEME_PALETTES[theme_name]
        pri = palette["primary"]

        self.title_lbl.configure(text_color=pri)
        self.header_frame.configure(border_color=pri)
        self.console.configure(border_color=pri)
        self.console.tag_config("primary", foreground=pri)

        self.theme_menu.configure(fg_color=palette["dark_bg"], button_color=pri, button_hover_color=palette["hover"])
        self.font_menu.configure(fg_color=palette["dark_bg"], button_color=pri, button_hover_color=palette["hover"])
        self.sort_menu.configure(fg_color=palette["dark_bg"], button_color=pri, button_hover_color=palette["hover"])

        self.btn_move_selected.configure(fg_color=palette["dark_bg"], hover_color=palette["dark_hover"], border_width=1, border_color=pri, text_color=pri if self.current_appearance == "Dark" else "#ffffff")

        if 0 <= self.focused_index < len(self.row_widgets):
            self._update_single_focus(self.focused_index, self.focused_index)

    def log(self, text, color_tag="primary"):
        self.console.insert("end", text + "\n", color_tag)
        self.console.see("end")

    def browse_directory(self):
        selected_dir = filedialog.askdirectory(initialdir=self.target_dir, title="Select Storage Directory to Analyze")
        if selected_dir:
            self.target_dir = os.path.abspath(selected_dir)
            self.dir_entry.delete(0, "end")
            self.dir_entry.insert(0, self.target_dir)
            self.save_config()
            self.refresh_file_list()

    def navigate_up(self):
        parent = os.path.dirname(self.target_dir)
        if parent and os.path.exists(parent) and parent != self.target_dir:
            self.target_dir = os.path.abspath(parent)
            self.dir_entry.delete(0, "end")
            self.dir_entry.insert(0, self.target_dir)
            self.save_config()
            self.refresh_file_list()

    def open_subfolder(self, folder_name):
        new_path = os.path.abspath(os.path.join(self.target_dir, folder_name))
        if os.path.isdir(new_path):
            self.target_dir = new_path
            self.dir_entry.delete(0, "end")
            self.dir_entry.insert(0, self.target_dir)
            self.save_config()
            self.refresh_file_list()

    def toggle_all_selection(self):
        if not self.file_vars: return
        new_val = not all(v.get() for v in self.file_vars.values())
        for var in self.file_vars.values():
            var.set(new_val)

    def on_sort_changed(self, selected_sort):
        self.current_sort = selected_sort
        self.displayed_count = 100
        self.save_config()
        self._render_file_list(self.scanned_items_data)

    def load_more_items(self):
        self.displayed_count += 100
        self._render_file_list(self.scanned_items_data)

    def refresh_file_list(self):
        if self.is_scanning: return
        custom_path = self.dir_entry.get().strip()
        if os.path.isdir(custom_path):
            self.target_dir = os.path.abspath(custom_path)

        if not os.path.exists(self.target_dir):
            self.log(f"[WARN] Target path not found: {self.target_dir}", "crimson")
            return

        self.is_scanning = True
        self.displayed_count = 100
        self.btn_refresh.configure(state="disabled", text="[SCANNING DIRECTORY...]")

        for widget in self.scroll_frame.winfo_children(): widget.destroy()
        self.file_vars.clear()
        self.row_widgets.clear()
        self.scanned_items_data.clear()

        threading.Thread(target=self._scan_thread_worker, daemon=True).start()

    def _scan_thread_worker(self):
        try:
            try:
                all_items = os.listdir(self.target_dir)
            except Exception as e:
                self.after(0, lambda: self.log(f"[ERROR] Access denied or unreadable path: {e}", "crimson"))
                all_items = []

            targets = [
                f for f in all_items 
                if f not in ("config.json", "app_icon.ico") 
                and not f.startswith('.') 
                and not f.endswith(('.py', '.pyw', '.ico', '.bat'))
            ]

            def process_single_item(name):
                item_path = os.path.join(self.target_dir, name)
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
            self.after(0, lambda: self._render_file_list(processed))
        except Exception as e:
            self.after(0, lambda: self.log(f"[CRITICAL ERROR] Scan worker failed: {e}", "crimson"))
            self.after(0, lambda: self._render_file_list([]))
        finally:
            self.is_scanning = False
            self.after(0, lambda: self.btn_refresh.configure(state="normal", text="[⟳ SCAN & ANALYZE DIRECTORY]"))

    def _render_file_list(self, raw_items):
        for widget in self.scroll_frame.winfo_children(): widget.destroy()
        self.file_vars.clear()
        self.row_widgets.clear()
        self.focused_index = 0

        f = FONT_PROFILES.get(self.current_font_profile, FONT_PROFILES["Retro Matrix (Consolas)"])
        if not raw_items:
            lbl = ctk.CTkLabel(self.scroll_frame, text="[!] DIRECTORY HAS NO ITEMS OR ALL ITEMS ARE < 1KB (FILTERED).", font=f["ui_bold"], text_color=self.text_muted)
            lbl.pack(pady=30)
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
            palette = THEME_PALETTES[self.current_theme_color]
            total_dir_size = sum(item[1] for item in sorted_items)

            for idx, (name, size_bytes, is_dir, _) in enumerate(self.current_display_items):
                icon_tag = "📁" if is_dir else "📄"
                size_str = format_size(size_bytes)
                var = ctk.BooleanVar(value=False)
                
                row_frame = ctk.CTkFrame(self.scroll_frame, fg_color="transparent", corner_radius=6)
                row_frame.pack(fill="x", padx=6, pady=2)

                chk = ctk.CTkCheckBox(
                    row_frame, 
                    text=f"{icon_tag} {name:<38} [{size_str:>10}]",
                    variable=var, 
                    font=f["file"], 
                    text_color=self.text_main,
                    fg_color=palette["primary"], 
                    hover_color=palette["hover"], 
                    checkmark_color="#080b0e"
                )
                chk.pack(side="left", padx=8, pady=4)

                btn_open = None
                if is_dir:
                    btn_open = ctk.CTkButton(
                        row_frame, 
                        text="[ 📂 OPEN ]", 
                        width=75, 
                        height=24, 
                        font=f["ui_sm"], 
                        fg_color="#1e293b", 
                        hover_color=palette["hover"],
                        command=lambda n=name: self.open_subfolder(n)
                    )
                    btn_open.pack(side="right", padx=8, pady=4)

                    row_frame.bind("<Double-Button-1>", lambda e, n=name: self.open_subfolder(n))
                    chk.bind("<Double-Button-1>", lambda e, n=name: self.open_subfolder(n))

                self.file_vars[name] = var
                self.row_widgets.append((row_frame, chk, btn_open))

            if len(sorted_items) > self.displayed_count:
                btn_more = ctk.CTkButton(
                    self.scroll_frame,
                    text=f"[ + SHOW MORE ITEMS ({len(sorted_items) - self.displayed_count} REMAINING) ]",
                    font=f["ui_bold"],
                    fg_color="#1e293b",
                    hover_color=palette["hover"],
                    command=self.load_more_items,
                    height=32
                )
                btn_more.pack(fill="x", padx=20, pady=8)

            if self.row_widgets:
                self._update_single_focus(0, 0)

            self.log(f"[SYS] Displaying top {len(self.current_display_items)} of {len(sorted_items)} items. Total space: {format_size(total_dir_size)}", "cyan")

    def cut_selected_items(self):
        selected_items = [name for name, var in self.file_vars.items() if var.get()]
        if not selected_items:
            messagebox.showwarning("No Items Selected", "Please select items you wish to cut.")
            return

        self.cut_clipboard_items = [os.path.join(self.target_dir, name) for name in selected_items]
        self.log(f"[CLIPBOARD] Cut {len(self.cut_clipboard_items)} item(s). Navigate to destination and click Paste or press Ctrl+V.", "gold")

    def paste_cut_items(self):
        if not self.cut_clipboard_items:
            messagebox.showinfo("Clipboard Empty", "No items in cut clipboard. Select files and click Cut first.")
            return

        self.log(f"[EXEC] Pasting {len(self.cut_clipboard_items)} item(s) to: {self.target_dir}", "gold")
        moved_count = 0

        for src in self.cut_clipboard_items:
            if not os.path.exists(src):
                continue
            item_name = os.path.basename(src)
            dst = os.path.join(self.target_dir, item_name)
            try:
                if src == dst:
                    continue
                shutil.move(src, dst)
                self.log(f"  └─► [MOVED] {item_name}", "primary")
                moved_count += 1
            except Exception as e:
                self.log(f"  └─► [FAIL] Could not move {item_name}: {e}", "crimson")

        self.cut_clipboard_items.clear()
        self.log(f"[SUCCESS] Paste complete: {moved_count} item(s) relocated.", "cyan")
        self.refresh_file_list()

    def move_selected_to_folder(self):
        target_subfolder = self.new_folder_entry.get().strip()
        selected_items = [name for name, var in self.file_vars.items() if var.get()]

        if not target_subfolder:
            messagebox.showwarning("Missing Destination", "Please provide a folder name to move files into.")
            return

        if not selected_items:
            messagebox.showwarning("No Items Selected", "Please select at least one item to move.")
            return

        dest_dir = os.path.join(self.target_dir, target_subfolder)
        os.makedirs(dest_dir, exist_ok=True)

        self.log(f"[EXEC] Moving {len(selected_items)} item(s) to: ./{target_subfolder}", "gold")
        moved_count = 0

        for item_name in selected_items:
            src = os.path.join(self.target_dir, item_name)
            dst = os.path.join(dest_dir, item_name)
            try:
                if src == dest_dir:
                    continue
                shutil.move(src, dst)
                self.log(f"  └─► [MOVED] {item_name}", "primary")
                moved_count += 1
            except Exception as e:
                self.log(f"  └─► [FAIL] Could not move {item_name}: {e}", "crimson")

        self.log(f"[SUCCESS] Operation finished: {moved_count} item(s) reorganized.", "cyan")
        self.new_folder_entry.delete(0, "end")
        self.refresh_file_list()

    def auto_categorize_files(self):
        raw_items = [item for item in self.scanned_items_data if not item[2]]
        if not raw_items:
            messagebox.showinfo("Auto Organize", "No files found to categorize in this directory.")
            return

        if not messagebox.askyesno("Confirm Auto Categorize", f"Organize {len(raw_items)} file(s) into category subfolders?"):
            return

        self.log("[EXEC] Commencing automated category sorting pipeline...", "gold")
        organized_count = 0

        for name, _, _, ext in raw_items:
            target_category = "Miscellaneous"
            for category_name, extensions in CATEGORY_RULES.items():
                if ext in extensions:
                    target_category = category_name
                    break

            cat_dir = os.path.join(self.target_dir, target_category)
            os.makedirs(cat_dir, exist_ok=True)

            src = os.path.join(self.target_dir, name)
            dst = os.path.join(cat_dir, name)

            try:
                shutil.move(src, dst)
                self.log(f"  └─► [{target_category}] {name}", "primary")
                organized_count += 1
            except Exception as e:
                self.log(f"  └─► [FAIL] {name}: {e}", "crimson")

        self.log(f"[SUCCESS] Auto-categorization finished: {organized_count} file(s) sorted.", "cyan")
        self.refresh_file_list()

    def delete_selected_items(self):
        selected_items = [name for name, var in self.file_vars.items() if var.get()]
        if not selected_items:
            messagebox.showwarning("No Items Selected", "Please select items you wish to purge.")
            return

        if not messagebox.askyesno("Confirm Permanent Deletion", f"Are you sure you want to permanently delete {len(selected_items)} selected item(s)?\nThis cannot be undone."):
            return

        self.log(f"[PURGE] Deleting {len(selected_items)} selected items...", "crimson")
        for item_name in selected_items:
            p = os.path.join(self.target_dir, item_name)
            try:
                if os.path.isdir(p):
                    shutil.rmtree(p)
                else:
                    os.remove(p)
                self.log(f"  └─► [DELETED] {item_name}", "ghost")
            except Exception as e:
                self.log(f"  └─► [FAIL] Could not delete {item_name}: {e}", "crimson")

        self.refresh_file_list()

if __name__ == "__main__":
    app = MatrixStorageManager()
    app.mainloop()
