"""
Unused code
"""
import re
# from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def ptt_webdriver(driver, url):
    """ 八卦版的文章需要驗證18歲，要透過Webdrive """
    driver.get(url)

    # If over 18 require
    try:
        over_18 = driver.find_element_by_class_name("over18-button-container")
        over_18 = over_18.find_element_by_class_name("btn-big")
        over_18.click()
    except NoSuchElementException:
        print("No over 18 require")

    try:
        # Get artical
        title = driver.find_elements_by_class_name("article-metaline")[1].text
        content = driver.find_element_by_id("main-content").text

        # Output file
        write_file(title, content)
    except IndexError:
        print(url + " no article")

def write_file(title, content):
    """ Write file """
    print(title)
    fout = open("D:/PTT/" + re.sub("[<>:\"/\\|?*]", " ", title) + ".txt", "w", encoding="UTF-8")
    fout.write(content)
    fout.close()
