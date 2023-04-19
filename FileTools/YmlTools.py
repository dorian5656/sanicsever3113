#! /usr/bin/env python
# -*-coding:utf-8-*-
import yaml


class Yml_Curd(object):
    """
    yml操作
    """

    def __init__(self, yml_path):
        self.yml_path = yml_path

    def read_yaml(self):
        """
        读取yml文件
        :return: 全部数据,为字典
        """
        with open(self.yml_path, 'r') as f:
            result = yaml.safe_load(f)
        # print(result)
        return result


# if __name__ == '__main__':
#     YC = Yml_Curd(R"demo_20230418.yml")
#     YC.read_yaml()
