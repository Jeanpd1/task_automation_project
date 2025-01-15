import time
import pyautogui

# Wait for user preparation
# This block gives the user 5 seconds to prepare before capturing the mouse position.
time.sleep(5)  # Wait for 5 seconds

# Print the current mouse position
# This captures and prints the current position of the mouse pointer.
print(pyautogui.position())

# Scroll the mouse wheel
# This scrolls the mouse wheel upward by 200 units. Use negative values to scroll downward.
pyautogui.scroll(200)