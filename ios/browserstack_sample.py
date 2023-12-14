from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
options = XCUITestOptions().load_capabilities({
    # Set URL of the application under test
    "app" : "bs://7d05390c0aaa28b5abe40e291c38440f62840243",

    # Specify device and os_version for testing
    "deviceName": "iPhone 12",
    "platformName": "ios",
    "platformVersion": "14",

    # Set other BrowserStack capabilities
    "bstack:options": {
        "userName" : "vitorcosta_z45hH6",
        "accessKey" : "1aZDLw7dRKb8rXpzgBxg",
        "projectName" : "Bees App IOS",
        "buildName" : "browserstack-build-1",
        "sessionName" : "BStack first_test"
    }
})

# Initialize the remote Webdriver using BrowserStack remote URL
# and options defined above
driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

# Just for validate test.
if 1==1:
	assert True
else:
	assert False

# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()