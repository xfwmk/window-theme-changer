import ctypes
import subprocess
import json
import os
import time
import winreg

print("Setting wallpaper to blue...")
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(
    SPI_SETDESKWALLPAPER,
    0,
    r"D:\Files\Pictures\planes\e726d802-fd37-4a11-abe7-2c615be846b2.png",
    3
)

OPENRGB = r"C:\Program Files\OpenRGB\OpenRGB.exe"
subprocess.Popen(
    [
        OPENRGB,
        "--server",
        "--server-port", "6742",
        "--startminimized"
    ],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    creationflags=subprocess.CREATE_NO_WINDOW
)
print("Setting Laptop Keyboard RGB to blue...")
subprocess.run(
    [
        OPENRGB,
        "--device", "1",
        "--mode", "static",
        "--color", "0000FF"
    ],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    creationflags=subprocess.CREATE_NO_WINDOW
)

subprocess.run('start "" "signalrgb://effect/applypreset/Solid%20Color/A?-silentlaunch-"', shell=True)

print("Setting terminal config to blue glass...")
time.sleep(1)

settings_path = os.path.expandvars(
    r"%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json"
)

with open(settings_path, "r", encoding="utf-8") as f:
    config = json.load(f)

for scheme in config.get("schemes", []):
    if scheme.get("name") == "Green Glass":
        scheme.update({
            "background": "#091C33",
            "black": "#091C33",
            "blue": "#7EB0FF",
            "brightBlack": "#355D8A",
            "brightBlue": "#A7D2FF",
            "brightCyan": "#A6E6FF",
            "brightGreen": "#6DA6FF",
            "brightPurple": "#8BB5FF",
            "brightRed": "#4E7CCF",
            "brightWhite": "#DCEBFF",
            "brightYellow": "#8FBFFF",
            "cursorColor": "#7EB0FF",
            "cyan": "#74C6FF",
            "foreground": "#1B4F8A",
            "green": "#4A7FD1",
            "purple": "#638FD8",
            "red": "#2E5EA8",
            "selectionBackground": "#2E5EA8",
            "white": "#A8C8F0",
            "yellow": "#5A90D8",
            "name": "Blue Glass"
        })

# Restore defaults
config["profiles"]["defaults"]["colorScheme"] = "Blue Glass"
config["profiles"]["defaults"]["cursorColor"] = "#1B4F8A"

for theme in config.get("themes", []):
    if theme.get("name") == "BlueTheme":
        theme["tab"]["background"] = "#19375AFF"
        theme["tabRow"]["background"] = "#091C33FF"

with open(settings_path, "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4)

print("Terminal theme restored to Blue Glass.")

#################################################