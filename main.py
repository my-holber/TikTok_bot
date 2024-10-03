from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)  # Prevents the browser from closing

# Initialize Chrome driver instance properly with options
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
           


# Navigate to the URL
driver.get('https://www.tiktok.com/explore?lang=fr')
time.sleep(9)
element = driver.find_element(By.ID, "header-login-button")
element.click()
# No driver.quit() to keep the browser open due to 'detach'
