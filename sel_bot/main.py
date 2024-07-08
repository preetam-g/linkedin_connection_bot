from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from configparser import ConfigParser
import csv
import time

file = "config.ini"
config = ConfigParser()
config.read(file)

LINKEDIN_USERNAME = config['linkedin']['LINKEDIN_USERNAME']
LINKEDIN_PASSWORD = config['linkedin']['LINKEDIN_PASSWORD']

CSV_NAME = "profiles.csv"

def login_to_linkedin(driver, username, password):
    """Logs into LinkedIn with the provided credentials."""
    driver.get('https://www.linkedin.com/login')

    # Wait for the username field to be present
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))
    )
    username_field.send_keys(username)

    # time.sleep(1)

    # Enter the password
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(password)

    # time.sleep(1)

    password_field.send_keys(Keys.RETURN)

    # Wait for the homepage to load
    WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.ID, 'global-nav-search'))
    )
    print("Logged in successfully")

    # time.sleep(1)


def Iterate_CSV(driver):
    try:

        with open(CSV_NAME, mode='r', newline='') as file:
            # Create a CSV reader object
            csv_reader = csv.reader(file)

            # Skip the header row
            next(csv_reader)

            # Iterate over the rows in the CSV
            for row in csv_reader:
                # Using the links  in the first column
                Send_Request(driver, row[0])

    except:
        pass

def Send_Request(driver, link):
    """Searches for clipboard content and clicks the first result link.
    Returns connection_request status and name of linkedin user"""

    driver.get(link)
    driver.maximize_window()
    time.sleep(2)

    try:
        
        more_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'More actions')]")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(more_button)).click()
        print("Clicked the More button")

        connect_now_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'to connect')]")

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(connect_now_button)).click()
        print("Clicked the Connect now button")

        time.sleep(2)
        # waiting 2 seconds and then clicking send with a note button
        send_without_note_button = driver.find_element(By.XPATH,
                                                       "//button[contains(@aria-label, 'Send without a note')]")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(send_without_note_button)).click()
        print("Clicked Send without note button")


    except:
        # When More button is not present
        try:

            # Wait for the Connect button to be present
            connect_now_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'to connect')]")

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(connect_now_button)).click()
            print("Clicked the Connect now button")

            time.sleep(2)
            # waiting 2 seconds and then clicking send with a note button
            send_without_note_button = driver.find_element(By.XPATH,
                                                           "//button[contains(@aria-label, 'Send without a note')]")
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(send_without_note_button)).click()
            print("Clicked Send without note button")



        except:
            print(f"Failed to connect")

    finally:
        # Ensure the driver is quit if it's still running
        try:
            driver.quit()
        except:
            pass


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
        Iterate_CSV(driver)
        wait_for_browser_close(driver)
    finally:
        # Ensure the driver is quit if it's still running
        try:
            driver.quit()
        except:
            pass


if __name__ == "__main__":
    main()