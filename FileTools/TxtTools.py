#! /usr/bin/env python
# -*-coding:utf-8-*-
class Txt_Curd(object):
    """
    文本操作
    """

    def __init__(self, txt_path, encoding="utf-8"):
        self.txt_path = txt_path
        self.enconding = encoding

    def read_txt(self):
        """
        读取文本
        :return: 返回数据为每行合并的列表
        """
        with open(self.txt_path, "r", encoding=self.enconding) as f:
            result = [line.strip() for line in f.readlines()]
        # print(result)

        return result


# if __name__ == '__main__':
#     txt_path = R"../TestFiles/TxtFiles/demo_20230418.txt"
#     TX = Txt_Curd(txt_path)
#     TX.read_txt()

