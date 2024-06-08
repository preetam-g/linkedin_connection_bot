from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import time


LINKEDIN_USERNAME = 'preetamgopalasetty@gmail.com'
LINKEDIN_PASSWORD = 'gp@linkedin'


def login_to_linkedin(driver, username, password):
    """Logs into LinkedIn with the provided credentials."""
    driver.get('https://www.linkedin.com/login')

    # Wait for the username field to be present
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))
    )
    username_field.send_keys(username)

    # Enter the password
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    # Wait for the homepage to load
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'global-nav-search'))
    )
    print("Logged in successfully")


def search_and_click_first_result(driver):
    """Searches for clipboard content and clicks the first result link."""

    # Get clipboard content
    # clipboard_content = pyperclip.paste()
    clipboard_content = "https://www.linkedin.com/in/royatrii//"

    # Enter the clipboard content into the search field
    driver.get(clipboard_content)
    driver.maximize_window()
    time.sleep(5)
    # btn = driver.find_element("tag_name","Button")
    #
    # driver.execute_script("arguments[0].click();",btn)
    # WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember91"]'))).click()
    # print("Button Clicked Successfully")

    try:

        # Wait for the Connect button to be present
        connect_now_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'to connect')]")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(connect_now_button)).click()
        print("Clicked the Connect now button")

        time.sleep(2)
        # waiting 2 seconds and then clicking send with a note button 
        send_without_note_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Send without a note')]")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(send_without_note_button)).click()
        print("Clicked Send without note button")


    except Exception as e:
        print(f"Failed to connect: {e}")
        import traceback
        traceback.print_exc()



def wait_for_browser_close(driver):
    """Keeps the script running until the browser window is closed."""
    while True:
        try:
            # Check if the driver is still active
            driver.current_url
            time.sleep(1)
        except:
            print("Browser closed, ending program.")
            break

def main():
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        login_to_linkedin(driver, LINKEDIN_USERNAME, LINKEDIN_PASSWORD)
        search_and_click_first_result(driver)
        wait_for_browser_close(driver)
    finally:
        # Ensure the driver is quit if it's still running
        try:
            driver.quit()
        except:
            pass

if __name__ == "__main__":
    main()