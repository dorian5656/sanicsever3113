#! /usr/bin/env python
# -*-coding:utf-8-*-
import yaml

# yml增删改查
class YmlCurd(object):
    """
    yml操作
    """

    def __init__(self, yml_path=""):
        self.yml_path = yml_path

    def read_yaml(self):
        """
        读取yml文件
        :return: 全部数据,为字典
        """
        with open(self.yml_path, 'r',encoding='utf-8') as f:
            result = yaml.safe_load(f)
        # print(result)
        return result


# if __name__ == '__main__':
#     YC = YmlCurd(R"demo_20230418.yml")
#     YC = YmlCurd(R"../ConfigTools/DatabaseConfig/PgServe.yml")
#     YC.read_yaml()
