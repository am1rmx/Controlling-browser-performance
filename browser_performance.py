from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

driver = Chrome(executable_path='chromedriver.exe')
driver.get('https://google.com')

search_bar = driver.find_element('name', 'q')
search_bar.send_keys('آموزش پایتون مکتب خونه')
search_bar.send_keys(Keys.ENTER)

# Wait for the search results to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'g')))

soup = BeautifulSoup(driver.page_source, 'html.parser')
name_list = soup.find_all('h3')

with open('names.txt', 'a', encoding='utf-8') as f:
    for name in name_list:
        f.write(name.text)
        f.write('\n')

driver.quit()