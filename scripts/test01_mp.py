import pytest

import api
from api.api_mp import ApiMp
from tool.read_yaml import read_yaml
from tool.tool import Tool
from tool.get_log import GetLog

log = GetLog.get_logger()


class TestMp:
    def setup_class(self):
        self.mp = ApiMp()

    # 多条数据参数化
    @pytest.mark.parametrize("username,password", read_yaml("mp_login.yaml"))
    def test01_mp_login(self, username, password):
        r = self.mp.api_mp_login(username, password)
        print("登录的结果为:", r.json())
        # 提取token
        # token = r.json().get("data").get("token")
        # token = r.json().get("access")
        # # 追加请求头
        # api.headers["Authorization"] = "Bearer " + token
        # print("添加token后的headers为：", api.headers)
        try:
            Tool.common_token(r)
            # Tool.common_assert(r,status_code=200)
        except Exception as e:
            # 写日志
            log.error(e)
            # 抛异常
            raise
        # # 状态码断言
        # assert 201 == r.status_code
        # # 业务信息断言
        # assert "OK" == r.json().get("message")

        # Tool.common_assert(r)

    # 一条数据参数化，用全局公共变量api.content
    def test02_mp_article(self, content=api.content):
        r = self.mp.api_mp_article(content)
        print("发布文章后的结果为:", r.json())
        try:
            Tool.common_assert_success(r)
        except Exception as e:
            # 写日志
            log.error(e)
            # 抛异常
            raise

    # 提取返回值到全局公共变量，便于下一个接口入参引用：api.user_id
    def test03_mp_users(self):
        r = self.mp.api_mp_users()
        print("查询所有用户信息后的结果为:", r.json())
        # 需要提取的变量，用于关联接口
        api.user_id = r.json()[0].get("id")
        print("提取返回的第一个user_id为：", api.user_id)
