# 用于快速测试某些操作。

from time import sleep

import ddddocr
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.get_driver import GetDriver
from flow.login.flow_login import FlowLogin
from page import url
from page.login.page_login import PageLogin


login = FlowLogin(GetDriver.get_driver())

login.flow_login("", "", "")
sleep(2)
