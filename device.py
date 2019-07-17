import subprocess
from config import driver

def scroll_down():
    width = driver().get_window_size()['width']
    height = driver().get_window_size()['height']

    driver().swipe(width*0.5, height*0.7, width*0.5, height*0.3, 400)

def execute_adb(command):
    subprocess.call(f'adb -s {driver().desired_capabilities["deviceUDID"]} {command}', shell=True)
