import api
import requests

from tool.get_log import GetLog

log = GetLog.get_logger()

"""
自媒体后台
"""


class ApiMp:
    def __init__(self):
        self.url_login = api.host + "/api/token/"
        log.info("正在初始化自媒体登录url: {}".format(self.url_login))

        self.url_article = api.host + "/myspace/post/"
        log.info("正在初始化自媒体发布文章url: {}".format(self.url_article))

        self.url_users = api.host + "/myspace/userlist/"
        log.info("正在初始化查询所有用户url: {}".format(self.url_users))

    def api_mp_login(self, username, password):
        data = {"username": username, "password": password}
        log.info("正在调用自媒体登录接口，请求数据：{}".format(data))
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    def api_mp_article(self, content):
        data = {"content": content}
        log.info("正在调用自媒体发布文章接口，请求数据：{} 请求头: {}".format(data, api.headers))
        return requests.post(url=self.url_article, json=data, headers=api.headers)

    def api_mp_users(self):
        data = {}
        log.info("正在调用自媒体查询所有用户接口，请求数据：{} 请求头: {}".format(data, api.headers))
        return requests.get(url=self.url_users, params=data, headers=api.headers)
