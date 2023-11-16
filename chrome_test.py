
from selenium import webdriver
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to Google.com
driver.get("https://www.google.com")

# Wait for search results to load
time.sleep(10)
driver.implicitly_wait(10)

# Find the search box element and enter "Samsung S24 Ultra"
search_box = driver.f
search_box.send_keys("Samsung S24 Ultra")

# Submit the search query
search_box.submit()

# Close the browser window
driver.quit()
