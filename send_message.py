import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class FacebookLogin:
    def __init__(self, email, password, headless=True):
        # Store credentials for login
        self.email = email
        self.password = password

        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        if headless:
            chrome_options.headless = True

        # Use chrome
        self.driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(),
            chrome_options=chrome_options,
        )
        LOGIN_URL = "https://www.facebook.com/login.php"
        self.driver.get(LOGIN_URL)
        time.sleep(1)  # Wait for some time to load

    def login(self):
        email_element = self.driver.find_element_by_id("email")
        email_element.send_keys(self.email)  # Give keyboard input

        password_element = self.driver.find_element_by_id("pass")
        password_element.send_keys(self.password)  # Give password as input too

        login_button = self.driver.find_element_by_id("loginbutton")
        login_button.click()  # Send mouse click

        time.sleep(2)  # Wait for 2 seconds for the page to show up

    def get_random_monkey(self):
        # random monkey url
        monkey_url = "https://www.placemonkeys.com/350/300?random"
        self.driver.get(monkey_url)
        time.sleep(1)
        body = self.driver.find_element_by_xpath("/html/body")
        body.send_keys(Keys.CONTROL, "a")
        body.send_keys(Keys.CONTROL, "c")

    def send_message(self, msg_url):
        self.get_random_monkey()
        self.driver.get(msg_url)
        time.sleep(1)
        text_bar = self.driver.find_element_by_xpath("//*[@data-editor]")
        text_bar.click()
        text_bar.send_keys(Keys.CONTROL, "v")
        text_bar.send_keys(Keys.ENTER)

        # wait for the image to be sent
        time.sleep(3)
        self.driver.close()


if __name__ == "__main__":
    # Facebook Login
    email = "OOOOOOOOOOO@gmail.com"
    pwd = "OOOOOOOOOOO"
    # Friend's Facebook message url
    msg_url = "https://www.facebook.com/messages/t/OOOOOOOOOOO"

    fb_login = FacebookLogin(email=email, password=pwd, headless=True)
    fb_login.login()
    fb_login.send_message(msg_url)
