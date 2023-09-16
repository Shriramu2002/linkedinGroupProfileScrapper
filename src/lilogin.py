from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class linkedInLogger:

    def __init__(self):
        self.browser = webdriver.Chrome();
        self.browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
        #Start using the functions after a delay
        self.browser.implicitly_wait(50)


    def login_to_linkedin(self, username, password):
        Username = self.browser.find_element(By.NAME, "session_key")
        #Send username details
        Username.send_keys(username)
        #Find password
        Password = self.browser.find_element(By.NAME, "session_password")
        #Send password details
        Password.send_keys(password)
        #Submit button
        self.browser.find_element(By.XPATH, "//button[@type='submit']").click()


    def getGroupNum(self, groupName):
        self.browser.get("https://linkedin.com/groups/")
        time.sleep(10)
        ul_element = self.browser.find_element(By.CLASS_NAME, "artdeco-list");
        a_elements = ul_element.find_elements(By.TAG_NAME, 'a')
        groupNum = ""

        for a_element in a_elements:
        # Get the text of the <a> tag
            link_text = a_element.text
            # Get the href attribute of the <a> tag
            link_href = a_element.get_attribute('href')
            if(link_text == groupName):
                groupNum = link_href.split('/')[4]

        return groupNum        


    def getCreds(self):
        cookies = self.browser.get_cookies();
        cusCookie = ""
        csrfToken = ""

        for cookie in cookies:
            cusCookie += f"{cookie['name']}={cookie['value']}; "
            if(cookie['name'] == "JSESSIONID"):
                csrfToken = cookie['value'][1:-1]

        return [cusCookie, csrfToken];




