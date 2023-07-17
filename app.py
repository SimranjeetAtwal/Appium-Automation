import sys
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
import time

# Configure the desired capabilities
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '',
    'deviceName': 'pixel_3a',
    'appPackage': 'com.linkedin.android',
    'appActivity': 'com.linkedin.android.authenticator.LaunchActivity'
}



# Configure the LinkedIn credentials
username = sys.argv[1]
password = sys.argv[2]

# Configure the profile URLs of the people you want to send connection requests , provide url starting from http://linkedin
profile_urls = [
    #'profile_link1',
    #'profile_link2',
    #'profile_link3'
]

# Initialize the Appium WebDriver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Wait for the LinkedIn app to load
time.sleep(15)

# Find and click the Sign In button
try:
    sign_in_button = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("Sign in")')
    sign_in_button.click()
    time.sleep(5)
except NoSuchElementException:
    pass

# Fill in the login form
email_input = driver.find_element(By.ID, 'com.linkedin.android:id/growth_login_join_fragment_email_address').send_keys(username)
password_input = driver.find_element(By.ID, 'com.linkedin.android:id/growth_login_join_fragment_password').send_keys(password)

sign_in_button = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("Continue")')
sign_in_button.click()

# Wait for the home screen to load
time.sleep(20)

# Send connection requests with messages
for profile_url in profile_urls:
    # Open the profile of the person
    driver.get(profile_url)
    time.sleep(5)

    overflow_button = driver.find_element(By.ACCESSIBILITY_ID, 'More options')
    # Tap on the overflow menu icon
    overflow_button.click()
    time.sleep(3)

    personalized_message_option = driver.find_element(By.XPATH, "//android.widget.TextView[@text='Personalize invite']")
    personalized_message_option.click()
    time.sleep(3)

    message_input = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
    message = "Hello , I would like to connect with you!"  # Replace with your personalized message
    message_input.send_keys(message)


    # Confirm the connection request
    send_button = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("Send")')
    send_button.click()
    time.sleep(10)

# Quit the driver
driver.quit()
