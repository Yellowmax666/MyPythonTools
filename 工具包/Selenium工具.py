from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys


def takeARest(sleepTime=1):
    time.sleep(sleepTime)


def 登入azure():
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches',['enable-automation'])

    # 打开网页
    driver = webdriver.Chrome(options=option)

    driver.get('https://portal.azure.cn/')

    # 输入账户
    takeARest(sleepTime=1)
    driver.find_element_by_css_selector('.form-control.ltr_override.input.ext-input.text-box.ext-text-box').send_keys("Max_huang@loreal.partner.onmschina.cn")

    # 点击下一步.win-button.button_primary.button.ext-button.primary.ext-primary
    driver.find_element_by_css_selector('.win-button.button_primary.button.ext-button.primary.ext-primary').click()

    # 输入密码
    takeARest(sleepTime=1)
    driver.find_element_by_css_selector('.form-control.input.ext-input.text-box.ext-text-box').send_keys("QAZ-cxz5600958")

    # 点击登录.win-button.button_primary.button.ext-button.primary.ext-primary[type="submit"]
    driver.find_element_by_css_selector('.win-button.button_primary.button.ext-button.primary.ext-primary[type="submit"]').click()

    driver.implicitly_wait(10)
    return driver




if __name__ == '__main__':
    登入azure()
    input("s")