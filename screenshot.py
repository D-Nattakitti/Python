import mss
import mss.tools

with mss.mss() as sct:
    # Capture the entire screen
    screenshot = sct.grab(sct.monitors[0])
    
    # Save the screenshot to a file
    mss.tools.to_png(screenshot.rgb, screenshot.size, output='screenshot.png')
    print("Screenshot saved as 'screenshot.png'")   