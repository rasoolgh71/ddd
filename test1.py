# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def set_chrome_driver():
    driver = webdriver.Chrome()
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("start-maximized")
    driver_options.add_argument("disable-infobars")
    driver_options.add_argument('--disk-cache-size=0')
    driver_options.add_argument('--ignore-certificate-errors')
    driver_options.add_argument('--ignore-ssl-errors')
    driver.scopes = ["https://www.instagram.com/.*"]
    driver.get("https://www.instagram.com")
    time.sleep(10)


def mobile_driver():
    chrome_options = Options()
    chrome_options.add_argument(
        '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.google.com')
    time.sleep(20)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # set_chrome_driver()
    mobile_driver()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
