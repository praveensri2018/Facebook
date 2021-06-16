from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time

option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

path = "F:\\cdweb\\chromedriver.exe"
driver = Chrome(options=option, executable_path= path)

driver.get("http://www.facebook.com")
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="pageFooter"]/ul/li[11]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="email"]').send_keys("enter your mail ID")
driver.find_element_by_xpath('//*[@id="pass"]').send_keys("enter your password")
time.sleep(1)
driver.find_element_by_name("login").click()
driver.find_element_by_xpath('//*[@aria-label="Account"]').click()
time.sleep(2)
driver.find_element_by_xpath('//div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[4]').click()
time.sleep(5)
driver.close()
