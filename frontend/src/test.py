import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Function to read credentials from a CSV file
def read_credentials(csv_file):
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        credentials = [row for row in csv_reader]
    return credentials

# Read credentials from the CSV file
csv_file = 'credentials.csv'
credentials = read_credentials(csv_file)

# Loop through each set of credentials
for cred in credentials:
    website = cred['website']
    username = cred['email']
    password = cred['password']

    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()

    # Open the website login page
    driver.get(website)
    driver.maximize_window()

    # Delay after opening the website
    time.sleep(2)  # Delay for 2 seconds

    # Locate the username field and enter the username
    user_name = driver.find_element(By.NAME, "email")
    user_name.send_keys(username)

    # Delay after entering the username
    time.sleep(2)  # Delay for 2 seconds

    # Locate the password field and enter the password
    user_pass = driver.find_element(By.NAME, "password")
    user_pass.send_keys(password)

    # Delay after entering the password
    time.sleep(2)  # Delay for 2 seconds

    # Locate and click the login button
    login_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Login']")
    login_button.click()

    # Delay after clicking the login button
    time.sleep(5)  # Delay for 5 seconds to observe the login result