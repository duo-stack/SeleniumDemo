from os import mkdir, remove, sep
from os.path import exists

import ddddocr

import base
import page.login as pl
from base.base import Base


class PageLogin(Base):
    def page_input_username(self, username: str):
        """
        输入用户名。
        :param username: 用户名。
        """
        self.base_input(pl.username, username)

    def page_get_username_message(self) -> str:
        """
        获得用户名输入框下面的错误提示。
        :return: 错误提示
        """
        return self.base_get_text(pl.username_message)

    def page_exists_username_message(self) -> bool:
        """获得用户名输入框下面的消息元素是否存在。"""
        return self.base_exists_element(pl.username_message)

    def page_input_password(self, password: str):
        """
        输入密码。
        :param password: 密码。
        """
        self.base_input(pl.password, password)

    def page_get_password_message(self) -> str:
        """
        获得密码输入框下面的错误提示。
        :return: 错误提示
        """
        return self.base_get_text(pl.password_message)

    def page_exists_password_message(self) -> bool:
        """获得密码输入框下面的消息元素是否存在。"""
        return self.base_exists_element(pl.password_message)

    def page_ocr_verify_code(self) -> str:
        """
        识别验证图，并返回验证码。
        :return: 验证码。
        """
        # 存储验证码图片
        verify_code = self.base_find_element(pl.verify_image)
        verify_code.screenshot(pl.verify_image_path)
        
        # 实例化 OCR，并传参不显示广告
        ocr = ddddocr.DdddOcr(show_ad=False)
        
        # 读取验证码图片，识别验证码
        with open(pl.verify_image_path, "rb") as f:
            verify_code = f.read()
        verify_code = ocr.classification(verify_code)
        
        # 删除验证码图片
        remove(pl.verify_image_path)
        
        return verify_code

    def page_input_verify_code(self, verify_code: str):
        """
        输入验证码。
        :param verify_code: 验证码。
        """
        self.base_input(pl.verify_code, verify_code)

    def page_click_verify_image(self):
        """点击验证图。"""
        self.base_click_js(pl.verify_image)

    def page_click_login(self):
        """点击登录按钮。"""
        self.base_click_js(pl.login)

    def page_save_full_screenshot(self, image_filename):
        """
        保存全屏截图。
        :param image_filename: 截图文件名。
        """
        image_path = base.screenshot_path + sep + pl.image_path
        if not exists(image_path):
            mkdir(image_path)
        self.base_save_full_screenshot(image_path + sep + image_filename)
