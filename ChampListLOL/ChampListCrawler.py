from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

url = "https://lol.garena.tw/game/champion"
driver.get(url)

wait = WebDriverWait(driver, 10)
elem = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "champlist-item__desc")))
# elem = driver.find_elements_by_class_name("champlist-item__desc")
with open("champ_list.txt", 'w', encoding='UTF-8') as fout:
    for e in elem:
        fout.write(e.text + '\n')
driver.close()
