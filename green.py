import ctypes
import subprocess
import json
import os
import time
import winreg

# Change wallpaper
print("Setting wallpaper to green...")
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(
    SPI_SETDESKWALLPAPER,
    0,
    r"D:\Files\Pictures\other\green.png",
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
print("Setting Laptop Keyboard RGB to green...")
subprocess.run(
    [
        OPENRGB,
        "--device", "1",
        "--mode", "static",
        "--color", "00FF00"
    ],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    creationflags=subprocess.CREATE_NO_WINDOW
)

subprocess.run('start "" "signalrgb://effect/applypreset/Solid%20Color/B?-silentlaunch-"', shell=True)

print("Setting terminal config to green glass...")
time.sleep(1)

settings_path = os.path.expandvars(
    r"%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json"
)

with open(settings_path, "r", encoding="utf-8") as f:
    config = json.load(f)

# Replace the existing Blue Glass scheme
for scheme in config.get("schemes", []):
    if scheme.get("name") == "Blue Glass":
        scheme.update({
            "background": "#062B12",
            "black": "#062B12",
            "blue": "#4FAF70",
            "brightBlack": "#1E5C35",
            "brightBlue": "#7BE39B",
            "brightCyan": "#8FFFC0",
            "brightGreen": "#55D17A",
            "brightPurple": "#70C98A",
            "brightRed": "#3B9E58",
            "brightWhite": "#D9FFE5",
            "brightYellow": "#79D995",
            "cursorColor": "#037403",
            "cyan": "#62D68A",
            "foreground": "#006600",
            "green": "#2E8B57",
            "purple": "#4EAD6B",
            "red": "#287A48",
            "selectionBackground": "#287A48",
            "white": "#A8E6B8",
            "yellow": "#5CBF75",
            "name": "Green Glass"
        })

# Update defaults to use new theme
config["profiles"]["defaults"]["colorScheme"] = "Green Glass"
config["profiles"]["defaults"]["opacity"] = 60
config["profiles"]["defaults"]["cursorColor"] = "#037403"

# Update tab colours
for theme in config.get("themes", []):
    if theme.get("name") == "BlueTheme":
        theme["tab"]["background"] = "#124A24FF"
        theme["tabRow"]["background"] = "#062B12FF"

# Save
with open(settings_path, "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4)

print("Terminal theme changed to Green Glass.")

#####################################################