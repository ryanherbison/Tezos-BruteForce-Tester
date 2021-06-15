from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# This script loads the tezos pwcheck web page and
# Cycles through a list of passwords 'ourlist.txt'
# Each passwords should be on it's own line.
# It cycles through each possible password
# and outputs the resulting tz1 address
# copy the output or redirect to a file
# save as a text file and use the second script
# to test against check.tezos
# Requirements are selenium WebDriver, Firefox, Python3.
# I used Archlinux your results may vary.

with webdriver.Firefox() as driver:

# Online/Or Save Webpage Locally
#   driver.get("https://tezos.com/static/pwcheck_full.html")
    driver.get("file:///home/ryan/bigdata-home/recovery/pwcheck_full.html");
    try:
      elem = WebDriverWait(driver, 10).until(
         EC.visibility_of_element_located((By.ID, "words"))
      )
      elem = driver.find_element_by_id("words")
# Set your passphrase here
      elem.send_keys('setup east quarter cat cage ring lumber swear brown swear they mean garden cradle hour')
      elem = driver.find_element_by_id("email")
# Set your email address here
      elem.send_keys('youremail@someemail.com')

      with open('ourlist.txt', 'r') as f:
        for passwordList in f:
          # Clear the TZ1 and Password Fields
          elem = driver.find_element_by_id("tz1").clear()
          elem = driver.find_element_by_id("password").clear()
          # Get Next Password
          elem = driver.find_element_by_id("password")
          elem.send_keys(passwordList.rstrip())
          # Sumbit the results
          elem.submit()
          # 1/4 second Delay
          sleep(0.25);
          # Get tz1 and output result
          result = driver.find_element_by_id("tz1").get_attribute("value")
          print(result,' ',passwordList.rstrip())

    finally:
      driver.quit()
