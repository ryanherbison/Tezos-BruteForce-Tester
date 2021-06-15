from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Requirements
# Selenium WebDriver, Firefox, Python3
# I used Arch Linux your results may vary
# This will check a list of TZ1's
# List of TZ1's must be a tz1 on each line of a text file
# The key below is valid for testing purposes
# If a match occurs you will see a result on every subsequent output line.
# You will see a value returned in a quantity of Tezos for that address/hash
# First match is the correct TZ1

#VALID KEY: tz1fz2aXLSgpuCYdQqMDumiSrEhTx9XRpAJY

with webdriver.Firefox() as driver:
    driver.get("https://check.tezos.com/");
    try:
      elem = WebDriverWait(driver, 10).until(
         EC.visibility_of_element_located((By.ID, "tz-key-input"))
      )

# Set your TZ1 File to check here

      with open('tz1-list.txt', 'r') as f:
        for tz1s in f:
          print(tz1s[0:36])
          first_chars = tz1s[0:36]
          # Clear Fields
          elem = driver.find_element_by_id("tz-key-input").clear()
          elem = driver.find_element_by_id("tz-key-input")
          elem.send_keys(first_chars)
          elem = driver.find_element_by_id("tz-submit").click()
          sleep(2);
          elem = driver.find_element_by_id("total-xtz")
          result = elem.get_attribute("innerHTML")
          print(result)

    finally:
      driver.quit()
