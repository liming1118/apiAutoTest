"""
公共变量
"""
from tool.read_yaml import read_yaml

host = "https://app165.acapp.acwing.com.cn"

headers = {"Content-Type": "application/json"}

# 一条数据参数化，用全局公共变量api.content
# 或者多个接口需要用到作为入参

data_article = read_yaml("mp_article.yaml")
print("发布文章的数据为，", data_article)  # [('发布一条内容',)]
# 文章内容
content = data_article[0][0]

# 需要提取的变量，用于关联接口
user_id = None
