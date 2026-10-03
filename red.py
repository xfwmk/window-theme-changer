import ctypes
import subprocess
import json
import os
import time
import winreg
import sys

print("Setting wallpaper to red...")
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(
    SPI_SETDESKWALLPAPER,
    0,
    r"D:\Files\Pictures\other\red.png",
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
print("Setting Laptop Keyboard RGB to red...")
subprocess.run(
    [
        OPENRGB,
        "--device", "1",
        "--mode", "static",
        "--color", "FF0000"
    ],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    creationflags=subprocess.CREATE_NO_WINDOW
)

subprocess.run('start "" "signalrgb://effect/applypreset/Solid%20Color/C?-silentlaunch-"', shell=True)

print("Setting terminal config to red glass...")
time.sleep(1)

settings_path = os.path.expandvars(
    r"%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json"
)

with open(settings_path, "r", encoding="utf-8") as f:
    config = json.load(f)

red_scheme = {
    "name": "Red Glass",
    "background": "#330909",
    "black": "#330909",
    "blue": "#FF7E7E",
    "brightBlack": "#8A3535",
    "brightBlue": "#FFA7A7",
    "brightCyan": "#FFA6A6",
    "brightGreen": "#FF6D6D",
    "brightPurple": "#FF8B8B",
    "brightRed": "#CF4E4E",
    "brightWhite": "#FFDCDC",
    "brightYellow": "#FF8F8F",
    "cursorColor": "#FF7E7E",
    "cyan": "#FF7474",
    "foreground": "#8A1B1B",
    "green": "#D14A4A",
    "purple": "#D86363",
    "red": "#A82E2E",
    "selectionBackground": "#A82E2E",
    "white": "#F0A8A8",
    "yellow": "#D85A5A"
}

# Ensure schemes list exists
config.setdefault("schemes", [])

# Update existing scheme or add a new one
found = False
for i, scheme in enumerate(config["schemes"]):
    if scheme.get("name") == "Red Glass":
        config["schemes"][i] = red_scheme
        found = True
        break

if not found:
    config["schemes"].append(red_scheme)

# Set defaults
config.setdefault("profiles", {}).setdefault("defaults", {})
config["profiles"]["defaults"]["colorScheme"] = "Red Glass"
config["profiles"]["defaults"]["cursorColor"] = "#8A1B1B"

# Optional: update theme colors if the theme exists
for theme in config.get("themes", []):
    if theme.get("name") == "BlueTheme":
        theme["tab"]["background"] = "#5A1919FF"
        theme["tabRow"]["background"] = "#330909FF"

with open(settings_path, "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4)

print("Terminal theme restored to Red Glass.")