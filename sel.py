from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from socket import timeout

chrome_options = Options()
chrome_options.add_argument("--user-agent={customUserAgent}")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
driver_path='chromedriver'
# driver=webdriver.Chrome(options=chrome_options,executable_path="chromedriver.exe")
# driver = webdriver.Chrome(options=chrome_options
s = Service(driver_path)

driver = webdriver.Chrome(options=chrome_options, service=s)
options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])


driver.get("https://quillbot.com/login")

time.sleep(15)
# Input_area = driver.find_element(by=By.XPATH, value="class='MuiFilledInput-input'")

# Input_area.send_keys("hello")

Input_area = driver.find_element(by=By.XPATH, value="//*[@id='mui-3']")
Input_area.send_keys("rajan@grimbyte.com")

Inputa_area = driver.find_element(by=By.XPATH, value="//*[@id='mui-4']")
Inputa_area.send_keys("Grimbyte123.")

Inputb_areb = driver.find_element(By.CLASS_NAME,"css-v7do75")
Inputb_areb.click()
# print(driver.page_source)
time.sleep(10)

Input_areac = driver.find_element(By.CLASS_NAME,'css-f958ss')
Input_areac.send_keys("hello dear")

button_press = driver.find_element(By.CLASS_NAME,'quillArticleBtn').click()
timeout = 20
try:
    myElem = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//button/div[text()="Rephrase"]')))
    
    print("paraphrase Page is ready!")
except TimeoutException:
    print("4Loading took too much time!")
Copy_Content = driver.find_element(by =By.XPATH,value="//*[@id='outputBottomQuillControls-default']").click()    
print("SuccessFully Login")
driver.quit()