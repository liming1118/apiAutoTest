import yaml

from config import BASE_PATH
import os


def read_yaml(filename):
    file_path = BASE_PATH + os.sep + "data" + os.sep + filename
    # 定义空列表，组装测试数据
    arr = []
    with open(file_path, "r", encoding="utf-8") as f:
        for datas in yaml.safe_load(f).values():
            # 列表里嵌入元组
            arr.append(tuple(datas.values()))
    return arr


if __name__ == '__main__':
    # print(read_yaml("mp_login.yaml"))  # [('123', '123')]
    print(read_yaml("mp_article.yaml"))
