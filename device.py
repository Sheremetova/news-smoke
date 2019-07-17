import subprocess
from config import App

def scroll_down():
    width = App.driver().get_window_size()['width']
    height = App.driver().get_window_size()['height']

    App.driver().swipe(0.5 * width,
                       0.7 * height,
                       0.5 * width,
                       0.3 * height,
                       400)

def execute_adb(command):
    subprocess.call(f'adb -s {App.driver().desired_capabilities["deviceUDID"]} {command}', shell=True)
