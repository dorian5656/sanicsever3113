#! /usr/bin/env python
# -*-coding:utf-8-*-
import hashlib


class Encipher_Curd(object):
    """
    密码相关的操作
    """

    def __init__(self):
        pass

    def confirm_password(self, stored_password_hash, password):
        """
        下载指定文件夹下的文件到本地文件夹
        :param stored_password_hash: 存储的密码哈希值
        :param password: 用户提供的密码
        :return:
        """
        # 将密码转换为字节串
        password_bytes = password.encode('utf-8')

        # 对输入的密码进行哈希计算
        provided_password_hash = hashlib.sha256(password_bytes).hexdigest()

        # 比对两个哈希值是否相同
        if provided_password_hash == stored_password_hash:
            # print(f"密码正确")
            return "密码正确"
        else:
            # print(f"密码错误")
            return "密码错误"

# if __name__ == '__main__':
#     stored_password_hash = "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"
#     password = "123456"
#     EC = Encipher_Curd()
#     EC.confirm_password(stored_password_hash, password)
