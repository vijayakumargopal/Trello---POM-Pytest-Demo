import pyautogui
import cv2
import numpy as np
import time


class ScreenRecorder:

    def __init__(self, file_name):
        self.resolution = pyautogui.size()
        self.resolution = (pyautogui.size().width, pyautogui.size().height)
        self.codec = cv2.VideoWriter_fourcc(*"MP4V")
        self.filename = file_name
        self.fps = 30.0
        self.out = cv2.VideoWriter(self.filename, self.codec, self.fps, self.resolution)
        self.stop_record = False

    def start_record(self):
        while True:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.out.write(frame)
            if self.stop_record:
                break

    def stop_record_loop(self):
        self.stop_record = True
        time.sleep(2)
        self.out.release()
