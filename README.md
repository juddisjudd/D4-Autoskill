# Diablo IV AutoSkill

Diablo IV AutoSkill is a Python script that automatically presses keys based on image matches on the screen. 

It uses OpenCV for image recognition and the pyautogui and keyboard libraries for key presses.

This script detects when specific images appear on the screen and automatically presses the corresponding keyboard keys. It only runs when a window with a specified PID is active.

## Features

- Configurable image-key mappings
- Enable or disable specific image-key mappings
- Only active when a specified window is in focus
- By default, the script tries to find the Diablo IV.exe process. Otherwise, you can specify the PID in the command line.

## Requirements

- Python 3
- OpenCV (`opencv-python`)
- NumPy
- PyAutoGUI
- PyScreenshot
- colorama
- psutils

## Installation

1. Install python https://www.python.org/downloads/
2. Install the required Python libraries:

```PowerShell
py -m pip install opencv-python numpy pyautogui pyscreenshot colorama psutil
```

## Usage
- Add your images to the images/ directory and update the config.json file with the image file names, keys to press, and optionally the "ignore" flag.
- **Run the script:** py autoskill.py or py autoskill.py -pid 20484 (specify you pid number)
- The script will continuously monitor the screen and press the corresponding key when an image match is found.
- To stop the script, press CTRL+C in the terminal.

## Customization
- To use different image file formats, update the image paths in the config.json file accordingly.
- To adjust the matching threshold, modify the threshold parameter in the find_image_on_screen function in the autoskill.py script.
- To adjust the key press duration, modify the time.sleep value between keyboard.press(key) and keyboard.release(key) in the main function in the autoskill.py script.

## Builded Autoskill
- In folder dist, is executable file. Change pictures and you can just run it.
