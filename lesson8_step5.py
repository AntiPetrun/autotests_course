# import time
#
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# time.sleep(5)
# browser.execute_script("document.title='Script executing';alert('Robots at work');")
# time.sleep(5)
# browser.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
