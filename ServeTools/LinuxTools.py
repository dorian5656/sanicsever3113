#! /usr/bin/env python
# -*-coding:utf-8-*-
import os
import paramiko
from FileTools.YmlTools import Yml_Curd


class ServeLink(object):
    """
    服务器连接和操作
    """

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def connect_test(self):
        """
        测试服务器连接
        :return:
        """
        # 实例化SSHClient
        client = paramiko.SSHClient()

        # 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 连接SSH服务端，以用户名和密码进行认证
        client.connect(hostname=self.host, port=self.port, username=self.username, password=self.password)

        # 打开一个Channel并执行命令
        stdin, stdout, stderr = client.exec_command('df -h ')  # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值

        # 打印执行结果
        print(stdout.read().decode('utf-8'))

        # 关闭SSHClient
        client.close()
        return r"connect success"

    def down_file(self, remote_folder_path, local_folder_path):
        """
        下载指定文件夹下的文件到本地文件夹
        :param remote_folder_path: 远程文件夹
        :param local_folder_path: 本地文件夹
        :return:
        """
        # 创建SSH客户端对象并连接
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=self.host, port=self.port, username=self.username, password=self.password)

        # 创建SFTP客户端对象并连接
        sftp_client = ssh_client.open_sftp()

        # 获取远程服务器上指定目录中的所有文件名
        remote_file_names = sftp_client.listdir(remote_folder_path)

        # 逐个下载文件到本地文件夹
        for remote_file_name in remote_file_names:
            remote_file_path = os.path.join(remote_folder_path, remote_file_name)
            local_file_path = os.path.join(local_folder_path, remote_file_name)
            sftp_client.get(remote_file_path, local_file_path)
            print(f'Saved {remote_file_name} to local directory.')

        # 关闭SFTP客户端和SSH客户端连接
        sftp_client.close()
        ssh_client.close()


# if __name__ == '__main__':
#     # 配置文件在yml中
#     YC = Yml_Curd(R"../TestFiles/YmlFiles/demo_20230418.yml")
#     result_yml = YC.read_yaml()
#     top = result_yml['servers']['top']
#     SL = ServeLink(top.get("host"), top.get("port"), top.get("username"), top.get("password"))
#     SL.connect_test() # 测试连接 df -h
#
#     remote_folder_path = R'/home/code/'  # 远程服务器文件夹路径
#     local_folder_path = R'../SaveFiles/Temp/'  # 本地保存文件路径
#     SL.down_file(remote_folder_path, local_folder_path)
