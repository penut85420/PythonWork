# -*- coding: utf-8 -*-
"""
Author: Penut
Date: 2018/01/27
"""
import re
import os
import urllib
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

WARNING_TEXT = "我們的系統偵測到您的電腦網路送出的流量有異常情況。這頁是為了確認要求確實出自您本人，不是由自動程式發出。"
COOKIES = {'over18': '1'}
PTT_URL = re.compile("www.ptt.cc/.*html")
PTT_CATEGORY = re.compile("www.ptt.cc/.*/")

def ptt_requests(url, keyword):
    """ Get PTT article through requests """
    try:
        soup = BeautifulSoup(requests.get(url, cookies=COOKIES).text, "html5lib")

        # Get title from url
        article_title = soup.find_all("span", {"class": "article-meta-value"})[2].text
        title = article_title + PTT_URL.search(url).group()[11:-5]
        category = PTT_CATEGORY.search(url).group()[15:-1]

        # Get article content
        divs = soup.find_all("div", {"id": "main-content"})
        content = ""
        for div in divs:
            content += div.text

        # Write article to file
        write_file(category, keyword, title, content)

    except IndexError:
        print(url + " no article")

def write_file(category, keyword, title, content):
    """ Write file """
    print(title)
    file_path = "D:/PTT/" + keyword[1:-1] + "/" + category + "/"
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    fout = open(file_path + re.sub("[<>:\"/\\\\|?*]", "_", title) + ".txt", "w", encoding="UTF-8")
    fout.write(content)
    fout.close()

def verify(driver):
    """ 可能發生人工驗證的部分先用手動的解決 """
    if driver.find_element_by_tag_name("body").text.find(WARNING_TEXT) > 0:
        print("需要人工驗證，完成後按任意鍵繼續")
        input()

def ptt_scrawler(keyword):
    """ Find a keyword in ptt """
    total = 0
    driver = webdriver.Firefox()
    keyword = '"' + keyword + '"'
    driver.get("https://www.google.com.tw/search?q="
               + urllib.parse.quote(keyword)
               + "+site:www.ptt.cc&num=100&start=0"
               + "&sa=N&biw=1304&bih=675")
    verify(driver)

    while True:
        google_results = driver.find_elements_by_class_name("g")
        total += len(google_results)

        for google_result in google_results:
            # Get ptt url
            url = google_result.find_element_by_tag_name("a").get_attribute("href")

            # Get ptt article
            ptt_requests(url, keyword)

        # Go next page
        try:
            driver.find_element_by_id("pnnext").click()
            verify(driver)
        except NoSuchElementException:
            break

    print("「%s」共搜尋到 %d 筆結果" % (keyword, total))
    driver.close()

def __main__():
    # Run to 賤貨
    words_list = ["賤婊", "婊子", "破麻", "賤婊子", "淫蕩", "淫娃", "賤貨", "賤女人", "賤人", "賤"]
    for w in words_list:
        ptt_scrawler(w)

__main__()
