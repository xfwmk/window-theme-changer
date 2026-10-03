import time
import sys
import os
import subprocess
import psutil
import socket

logo = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡇
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣟⡇
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣟⡾⡇
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣻⢾⣟⡇
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⣯⣟⡿⣾⠇
 ⢰⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⢿⣽⣷⣻⢿⡽⡇
 ⠀⠀⠁⠙⠺⠳⡿⣞⣷⣻⢾⣳⣟⡾⣷⣻⣞⡷⣟⣾⡽⣿⣞⡷⣿⢯⣿⠇
 ⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠿⠽⣯⢿⣽⢷⣻⣟⣯⡿⣽⣷⣻⢿⡽⣿⢾⡇
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠏⢿⣾⢯⣟⣷⣯⣟⣯⡿⣯⣿⡆
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠞⢷⢯⣿⡽⣷⣻⡆
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠫⢷⡇"""

def loading_bar(duration=5, length=30):
    for i in range(length + 1):
        percent = (i / length) * 100
        bar = '#' * i + '-' * (length - i)
        sys.stdout.write(f"\r[{bar}] {percent:.2f}%")
        sys.stdout.flush()
        time.sleep(duration / length)
    print()

#def loop():
#    os.system("clear")
#    print(logo)
#    print("Retrieving system information...")
#    loading_bar()
#    for x in range(999):
#        os.system("clear")
#        print(logo)
#        time.sleep(1)
#        cpu()
#        time.sleep(1)
#        gpu()
#        time.sleep(1)
#        memory()
#        time.sleep(1)
#        disk()
#        time.sleep(1)
#        network()
#        time.sleep(30)

def main():
    os.system("clear")
    gpu()
    disk()
    cpu()
    network()

def slowtext(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def cpu():
    memory = psutil.virtual_memory()
    #print("== CPU Information ==           ")
    #print(f"Physical cores: {psutil.cpu_count(logical=False)}    ") 
    print(f"Logical cores: {psutil.cpu_count(logical=True)}                    ") 
    print(f"CPU usage: {psutil.cpu_percent(interval=1)}%                      == Memory Information ==")
    print(f"                                      Total: {memory.total / (1024**3):.2f} GB")

def gpu():
    print("⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡇        == GPU Information ==")
    try:
        result = subprocess.run(['nvidia-smi', '--query-gpu=name,memory.total,memory.used,memory.free,utilization.gpu', '--format=csv,noheader,nounits'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            gpu_info = result.stdout.strip().split('\n')
            for i, info in enumerate(gpu_info):
                name, total_mem, used_mem, free_mem, utilization = info.split(', ')
                print(f" ⠀⠀⠀⠀⠀⠀⠀ ⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣟⡇        GPU {i}: {name}")
                print(f"⠀⠀⠀⠀⠀⠀⠀ ⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣟⡾⡇        Total Memory: {total_mem} MB")
                print(f"⠀⠀⠀⠀⠀⠀ ⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣻⢾⣟⡇        Used Memory: {used_mem} MB")
                print(f"⠀⠀⠀⠀⠀ ⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⣯⣟⡿⣾⠇        Utilization: {utilization}%")
                print(f"   ⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⢿⣽⣷⣻⢿⡽⡇    ")
        else:
            print("No NVIDIA GPU detected or nvidia-smi not found.")
    except FileNotFoundError:
        print("nvidia-smi command not found. Please ensure NVIDIA drivers are installed.")

def memory():
    print("== Memory Information ==")
    memory = psutil.virtual_memory()
    print(f"Total: {memory.total / (1024**3):.2f} GB")
    print(f"Available: {memory.available / (1024**3):.2f} GB")
    print(f"Used: {memory.used / (1024**3):.2f} GB")
    print(f"Percentage: {memory.percent}%")

def disk():
    print("⠀  ⠀⠁⠙⠺⠳⡿⣞⣷⣻⢾⣳⣟⡾⣷⣻⣞⡷⣟⣾⡽⣿⣞⡷⣿⢯⣿⠇        == Disk Information ==")
    disk = psutil.disk_usage('/')
    print(f"⠀⠀⠀ ⠀⠀⠀ ⠀⠈⠉⠛⠿⠽⣯⢿⣽⢷⣻⣟⣯⡿⣽⣷⣻⢿⡽⣿⢾⡇        Total: {disk.total / (1024**3):.2f} GB")
    print(f"⠀⠀⠀ ⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠈⠉⠛⠏⢿⣾⢯⣟⣷⣯⣟⣯⡿⣯⣿⡆        Used: {disk.used / (1024**3):.2f} GB")
    print(f"⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠉⠛⠞⢷⢯⣿⡽⣷⣻⡆        Free: {disk.free / (1024**3):.2f} GB")
    print(f"== CPU Information ==⠀⠀  ⠈⠛⠫⢷⡇        Percentage: {disk.percent}%")

def network():
    memory = psutil.virtual_memory()
    print(f"== Network Information ==             Available: {memory.available / (1024**3):.2f} GB")
    net = psutil.net_io_counters()
    print(f"Bytes sent: {net.bytes_sent / (1024**2):.2f} MB                 Used: {memory.used / (1024**3):.2f} GB")
    print(f"Bytes received: {net.bytes_recv / (1024**2):.2f} MB             Percentage: {memory.percent}%")


## MAIN ##
#loop()

main()