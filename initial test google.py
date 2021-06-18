
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep
browser = webdriver.Firefox()
browser.get('https://www.google.com/?gws_rd=ssl')


try:
    Ginput: webdriver.Firefox = browser.find_element_by_name('q')
    Ginput.send_keys(' روزی که که ممد داد؛ ... آب را. منحرفه سگ')
    Ginput.send_keys(Keys.RETURN)
    print('element found')
except NoSuchElementException:
    print('no such element')

sleep(5)
browser.find_element_by_css_selector("h3.LC20lb").click()
for i in range(10):
    print(f'closing in {i+1} / 10 . . . ')
    sleep(1)
    
print('complete')
browser.quit()
