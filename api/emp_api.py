import requests

import app


class EmpApi:

    def __init__(self):
        self.emp_url = app.HOST + "/api/sys/user"
        # 调用员工管理模块相关接口时，先调用Login.py接口获取到的app.HEADERS才会是令牌
        self.headers = app.HEADERS

    def add_emp(self, username, mobile):
        data = {"username": username,
                "mobile": mobile,
                "timeOfEntry": "2019-12-02",
                "formOfEmployment": 1,
                "workNumber": "1234",
                "departmentName": "测试",
                "departmentId": "1210411411066695680",
                "correctionTime": "2019-12-15T16:00:00.000Z"
                }
        # 发送添加员工接口请求
        response = requests.post(self.emp_url, json=data, headers=self.headers)
        # 返回添加员工接口的响应数据
        return response

    def query_emp(self):
        '''查询员工信息'''
        # 查询员工的URL结构是 http://182.92.81.159/api/sys/user/1234455678654
        # 所以拼接URL时要加“/”
        url = self.emp_url + "/" + app.EMP_ID
        return requests.get(url, headers = self.headers)

    def modify_emp(self, username):
        # 修改员工的URL结构是 http://182.92.81.159/api/sys/user/1234455678654
        # 所以拼接URL时要加“/”
        url = self.emp_url + "/" + app.EMP_ID
        # 从外部接受修改的username，拼接成json数据
        data = {
            "username":username
        }
        # 返回查询结果
        return requests.put(url, json=data, headers=self.headers)

    def delete_emp(self):
        url = self.emp_url + "/" + app.EMP_ID
        return requests.delete(url, headers=self.headers)
