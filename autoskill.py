import sys
import cv2
import numpy as np
import pyautogui
import json
import time
import ctypes
import psutil
from colorama import init, Fore
import mss
import mss.tools

init(autoreset=True)

def load_config():
    with open("config.json", "r") as f:
        config = json.load(f)

    config["matches"] = [match for match in config["matches"] if match.get("enabled", True)]

    return config

def find_image_on_screen(template, threshold=0.99):
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)
        screen = np.array(screenshot)

    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        return max_loc

    return None

def is_target_window_active(process_pid):
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    pid = ctypes.wintypes.DWORD()
    ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.pointer(pid))
    return pid.value == process_pid

def get_target_pid(config):
    process_name = config.get("process_name")
    if process_name:
        for proc in psutil.process_iter(['name', 'pid']):
            if proc.info['name'] == process_name:
                return proc.info['pid']
    return None

def main(config, target_pid):
    verbose = config.get("verbose", True)

    while True:
        if not is_target_window_active(target_pid):
            if verbose:
                print(Fore.YELLOW + "Target window is not active")
            time.sleep(1)
            continue

        match_found = False
        for match in config["matches"]:
            image = cv2.imread(match["image"], cv2.IMREAD_COLOR)
            if find_image_on_screen(image, threshold=config["picture_match"]) is not None:
                match_found = True
                if verbose:
                    print(Fore.GREEN + f"Match found for {match['image']}, pressing key {match['key']}")
                pyautogui.press(match["key"])

        if not match_found:
            if verbose:
                print(Fore.RED + "No match found")

        time.sleep(0.1)

if __name__ == "__main__":
    config = load_config()

    target_pid = get_target_pid(config)

    if target_pid is None:
        print(Fore.RED + "Target process not found.")
    else:
        main(config, target_pid)
