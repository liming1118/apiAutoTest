import api
from tool.get_log import GetLog

log = GetLog.get_logger()


class Tool:
    # 1. 提取token
    @classmethod
    def common_token(cls, response):
        # 提取token
        token = response.json().get("access")
        # 追加请求信息头 字典有则更新，有则新增
        api.headers['Authorization'] = "Bearer " + token
        log.info("正在提取token， 提取后的header为：{}".format(api.headers))

        print("添加token后的headers为：", api.headers)

    # 2. 断言 （根据实际接口返回设计）
    @classmethod
    def common_assert(cls, response, status_code=201):
        log.info("正在调用公共断言方法！")

        # 断言状态码 不传默认断言201
        assert status_code == response.status_code
        # 断言响应信息
        assert "OK" == response.json().get("message")

    @classmethod
    def common_assert_success(cls, response):
        log.info("正在调用断言success方法！")
        assert "success" == response.json().get("result")

