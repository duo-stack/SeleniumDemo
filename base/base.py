import logging
from os import mkdir
from os.path import exists

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

import base


class Base:
    def __init__(self, driver):
        self.driver = driver
        # self.driver.set_page_load_timeout(10)

        self.logger = logging.getLogger('POC')
        if not self.logger.handlers:
            self.logger.setLevel(logging.INFO)
            file_handler = logging.FileHandler(filename=base.log_path,
                                               mode="w")
            formatter = logging.Formatter(
                fmt="%(asctime)s - %(levelname)s - %(filename)s - "
                    "%(funcName)s: %(lineno)s line - %(message)s",
                datefmt="%Y/%m/%d %H:%M:%S")
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

        if not exists(base.screenshot_path):
            mkdir(base.screenshot_path)

    def base_find_element(self, locator, timeout=10, poll=0.5):
        """
        定位元素，0.5秒一次，10秒超时。
        :param locator: eg. (By.CSS_SELECTOR, "#username").
        :param timeout: 超时时间，可选参数，默认10秒。
        :param poll: 每隔poll秒定位一次，可选参数，默认为0.5。
        :return: element
        """
        return WebDriverWait(
            self.driver, timeout=timeout, poll_frequency=poll
        ).until(lambda dr: dr.find_element(*locator))

    def base_input(self, locator, value: str):
        """
        在元素中输入内容。
        :param locator: eg. (By.CSS_SELECTOR, "#username").
        :param value: 要输入的内容。
        """
        element = self.base_find_element(locator)
        element.clear()
        ActionChains(self.driver).move_to_element(
            element).click(element).send_keys(value).perform()
        # element.send_keys(value)

    def base_input_no_clear(self, locator, value: str):
        """
        在元素中输入内容，输入前不做清空操作。
        :param locator: eg. (By.CSS_SELECTOR, "#username").
        :param value: 要输入的内容。
        """
        element = self.base_find_element(locator)
        ActionChains(self.driver).move_to_element(
            element).click(element).send_keys(value).perform()
        # element.send_keys(value)

    def base_click(self, locator):
        """
        直接对元素进行点击操作，浮窗类内容可能无法被触发。
        :param locator: eg. (By.CSS_SELECTOR, "#username").
        """
        self.base_find_element(locator).click()

    def base_click_js(self, locator):
        """
        模拟js进行点击操作，可以触发浮窗类内容。
        :param locator: eg. (By.CSS_SELECTOR, "#username").
        """
        element = self.base_find_element(locator)
        ActionChains(self.driver).move_to_element(
            element).click(element).perform()

    def base_drag(self, locator, distance: tuple):
        """
        模拟js进行拖拽。
        :param locator: eg. (By.CSS_SELECTOR, "#username").
        :param distance: 要拖拽的距离，横向距离和纵向距离。
        """
        element = self.base_find_element(locator)
        ActionChains(self.driver).move_to_element(
            element).click_and_hold(element).perform()
        ActionChains(self.driver).move_by_offset(*distance).perform()
        ActionChains(self.driver).release().perform()

    def base_get_text(self, locator) -> str:
        """
        获得元素的文本，即标签语言中间夹着的内容。
        :param locator: eg. (By.CSS_SELECTOR, "#username").
        """
        return self.base_find_element(locator).text.strip()

    def base_get_attribute(self, locator, attribute: str) -> str:
        """
        获得元素的title属性。
        :param locator: eg. (By.CSS_SELECTOR, "#username").
        :param attribute: 需要获得的属性名。
        """
        element = self.base_find_element(locator)
        return element.get_attribute(attribute).strip()

    def base_save_full_screenshot(self, image_path: str):
        """
        浏览器窗口内全屏截图并保存。
        :param image_path: 保存截图文件的文件名，.png格式。
        """
        self.driver.save_screenshot(image_path)

    def base_exists_element(self, locator) -> bool:
        """
        元素是否存在。使用find_elements定位元素，长度为0则认为元素不存在。
        :param locator: eg. (By.CSS_SELECTOR, "#username").
        """
        elements = self.driver.find_elements(*locator)
        if len(elements):
            return True
        else:
            return False

    def base_get_element_count(self, locator) -> int:
        """
        获得指定locator的元素的个数。
        :param locator: eg. (By.CSS_SELECTOR, "#username").
        """
        return len(self.driver.find_elements(*locator))
