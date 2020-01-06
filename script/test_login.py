import unittest, logging

from api.login_api import LoginApi
from utils import assert_common


class TestIHRMLogin(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        # 初始化登录类
        cls.login_api = LoginApi()

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test01_login_success(self):
        '''登录成功'''
        # 调用封装的登录接口
        response = self.login_api.login('13800000002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 调用输出登录接口返回的数据
        logging.info("登录成功接口返回的数据为：{}".format(jsonData))

        # 断言
        # self.assertEqual(200, response.status_code)  # 断言响应状态码
        # self.assertEqual(True, jsonData.get("success"))  # 断言success
        # self.assertEqual(10000, jsonData.get("code"))  # 断言code
        # self.assertIn("操作成功", jsonData.get("message"))  # 断言mess

        assert_common(self, response, 200, True, 10000, "操作成功")

    def test02_username_is_not_exist(self):
        '''账号不存在'''
        # 调用封装的登录接口
        response = self.login_api.login("13900000002", "123456")
        # 接收返回的json数据
        jsonData = response.json()
        # 调用输出登录接口返回的数据
        logging.info("账号不存在返回的数据：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test03_password_error(self):
        '''密码错误'''
        # 调用封装的登录接口
        response = self.login_api.login("13800000002", "123455")
        # 接收返回的json数据
        jsonData = response.json()
        # 调用输出登录接口返回的数据
        logging.info("密码错误：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test04_account_spechars(self):
        '''账号含有特殊字符'''
        # 调用封装的登录接口
        response = self.login_api.login("！@#￥%……&*（）", "123456")
        # 接收返回的json数据
        jsonData = response.json()
        # 调用输出登录接口返回的数据
        logging.info("账号输入特殊字符：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test05_account_empty(self):
        '''账号为空'''
        # 调用封装的登录接口
        response = self.login_api.login("", "123456")
        # 接收返回的json数据
        jsonData = response.json()
        # 调用输出登录接口返回的数据
        logging.info("账号为空：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")