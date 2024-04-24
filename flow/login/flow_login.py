from time import sleep

from page.login.page_login import PageLogin


class FlowLogin(PageLogin):
    def flow_login(self, username, password, verify_code=None):
        """
        执行完整的登录操作。
        :param username: 用户名。
        :param password: 密码。
        """
        self.page_click_verify_image()
        sleep(1)
        self.page_input_username(username)
        self.page_input_password(password)
        if verify_code is None:
            verify_code = self.page_ocr_verify_code()
            while len(verify_code) != 4:
                self.page_click_verify_image()
                sleep(1)
                verify_code = self.page_ocr_verify_code()
        self.page_input_verify_code(verify_code)
        self.page_click_login()
