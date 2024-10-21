import cv2
import numpy as np
import pyautogui
from pynput import keyboard
from pynput.mouse import Button, Controller
import time

# Global variable to control auto-clicking
clicking = False

# Mouse controller
mouse_controller = Controller()

def on_press(key):
    global clicking
    try:
        if key.char == 's':
            clicking = True
            print("Auto-clicking started.")
        elif key.char == 'p':
            clicking = False
            print("Auto-clicking stopped.")
    except AttributeError:
        pass

def auto_click(x, y):
    mouse_controller.position = (x, y)
    mouse_controller.click(Button.left, 1)

def masking_warna_screenshot(hex_color, region, min_area, max_area):
    bgr_color = np.uint8([[hex_to_bgr(hex_color)]])
    hsv_color = cv2.cvtColor(bgr_color, cv2.COLOR_BGR2HSV)
    target_hsv = hsv_color[0][0]
    lower_bound = np.array([target_hsv[0] - threshold, 100, 100])
    upper_bound = np.array([target_hsv[0] + threshold, 255, 255])

    while True:
        screenshot = np.array(pyautogui.screenshot(region=region))
        frame = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
        ignore_start = 175 - region[1]
        ignore_end = 205 - region[1]
        frame[ignore_start:ignore_end, :, :] = 0

        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)
        result = cv2.bitwise_and(frame, frame, mask=mask)

        if clicking:
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                area = cv2.contourArea(contour)
                if min_area <= area <= max_area:
                    M = cv2.moments(contour)
                    if M["m00"] != 0:
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])
                        auto_click(cX + region[0], cY + region[1])
            time.sleep(0.0000000000000000001)

        cv2.imshow("Masked Image", mask)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

def hex_to_bgr(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (4, 2, 0))

hex_color = "#fe3e6c"
region = (720, 155, 475, 620)
threshold = 10  # Adjust the threshold as needed
min_area = 1200  # Minimum contour area to consider
max_area = 1000000000  # Maximum contour area to consider

listener = keyboard.Listener(on_press=on_press)
listener.start()

masking_warna_screenshot(hex_color, region, min_area, max_area)
