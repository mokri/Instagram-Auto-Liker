from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstaBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

# login into account
    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(3)

        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        time.sleep(3)
        user_pwd_elem = driver.find_element_by_xpath("//input[@name='password']")
        user_pwd_elem.clear()
        user_pwd_elem.send_keys(self.password)

        user_pwd_elem.send_keys(Keys.RETURN)

# escape notification pop up
    def escape_notification(self):
        time.sleep(3)
        driver = self.driver
        driver.get('https://www.instagram.com/'+self.username)

# view stories
    def view_stories(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/stories/tags/'+hashtag+'/')
        time.sleep(10)
# go back to home (user profile)
    def go_back_home(self):
        driver = self.driver
        driver.get('https://www.instagram.com/'+self.username)
        time.sleep(3)

# like photo
    def like_photo(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/'+hashtag+'/')
        time.sleep(4)

        for i in range(1, 3):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(2)

        #search for pics links

        hrefs = driver.find_element_by_tag_name('a')

        elems = driver.find_elements_by_xpath("//a[@href]")
        pic_hrefs = [href.get_attribute("href") for href in elems if '/p/' in href.get_attribute("href")]
        random.shuffle(pic_hrefs)

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(4)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

# extract the like (heart) button
            try:
                driver.find_element_by_class_name('wpO6b').click()
                time.sleep(15)
                driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(20)
            except Exception :
                time.sleep(2)
