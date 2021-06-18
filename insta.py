
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep



def ss(s):print(f"***{s}***\n");

class INSTAGRAM:
    
    
    

    def __init__(self, *args, **kwargs):
        self.firefox = webdriver.Firefox()
        self.username = 'siadevacc1'
        self.password = 'siadevaccsiadevacc'


    def _open_instagram(self, *args, **kwargs):
        self.firefox.get('https://www.instagram.com')
        self.firefox.implicitly_wait(1)
        
    def _login_fill_submit(self, *args, **kwargs):

        try:
            usernameinput = self.firefox.find_element_by_name('username')
            passwordinput = self.firefox.find_element_by_name('password')
            ss('login inputs were found ... ')
        except: ss('elements no found') ;

        usernameinput.clear()
        usernameinput.send_keys(str(self.username))
        self.firefox.implicitly_wait(1)
        passwordinput.clear()
        passwordinput.send_keys(str(self.password))
        self.firefox.implicitly_wait(1)
        passwordinput.submit()
        sleep(3)

    def _silence_intro_modal(self,*args, **kwargs):
        try:

            self.firefox.find_element_by_css_selector('button.HoLwm').click()
            ss('notification modal silenced')
        except NoSuchElementException: ss('no modal ... good to go ...')

    def login(self, *args, **kwargs):
        try:
            self._open_instagram()
            self._login_fill_submit()
            self._open_instagram()
            self._silence_intro_modal()
            ss('login was a "SUCCESS" ')

        except: ss('login FAILED')


    def _push_follow_btn(self, *args, **kwargs):
        try:
            btn = self.firefox.find_element_by_css_selector('button.jIbKX')
            btn.click()
        except: ss('follow btn not found')




        


bot = INSTAGRAM()

bot.login()