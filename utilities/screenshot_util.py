import os
from datetime import datetime
from selenium.webdriver.remote.webdriver import WebDriver

def capture_screenshot(driver: WebDriver, test_name: str):
    """
    Capture a screenshot with timestamp and save in /screenshots folder at project root.
    Safe to call even if driver is None or saving fails (won't raise).
    """
    try:
        if not driver:
            print(" capture_screenshot called with no driver (None).")
            return

        # Build screenshots folder at project root (one level above utilities/)
        base_dir = os.path.dirname(os.path.abspath(__file__))  # utilities/
        project_root = os.path.dirname(base_dir)
        screenshots_dir = os.path.join(project_root, "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        safe_test_name = test_name.replace(" ", "_").replace("::", "_")
        file_name = f"{safe_test_name}_{timestamp}.png"
        file_path = os.path.join(screenshots_dir, file_name)

        driver.save_screenshot(file_path)
        print(f" Screenshot saved: {file_path}")
    except Exception as e:
        # Never raise from screenshot capture — just log
        print(f" Failed to capture screenshot: {e}")
