# sanicserve3113

## 介绍
```
基于python3.11.3

封装一些常用的工具包

提高开发效率
```
## 文件结构

```python
sanicserve3113/  			# 顶级包
    	__init__.py
├─ConfigTools				# 配置包	
│  └─DatabaseConfig				# 数据库配置
│          PgServe.yml			# Pg服务器
│          SanquServe.yml		# 三区服务器
│          
├─CrawlerTools				# 爬虫包
│      DlzbCrawler.py			# 电力招标网
│      __init__.py	
│      
├─DatebaseFile				# 数据库包
│      wtinfo.xlsx				# wtif表格
│      
├─DatebaseTools				# 数据库包
│      PgTools.py				# Pg
│      __init__.py
│      
├─DingtalkTools				# 钉钉包
│      DingtalkBot.py			# 机器人
│      __init__.py
│      
├─FileTools					# 常用文件包
│  │  ExcleTools.py				# 表格
│  │  FolderTools.py			# 文件夹
│  │  YmlTools.py				# yml
│  │  ZipTools.py				# zip
│  │  __init__.py
│ 
├─ProjectCollection				    # 项目入口
│  │  ServerDownloadFileParsing.py	# 服务器下载文件解析			
│  │  __init__.py
│ 
├─ServeTools				# 服务器包
│      LinuxTools.py			# linux
│      __init__.py
│      
├─Temp						# 临时文件夹
└─TimeTools					# 时间包
    │  DatetimeTools.py			# 时间
    │  __init__.py
     

            

```
## 代码规范(试用版)
1. 变量命名

   一个单词组成: 小写 *connect* 

   多个单词组成: 下划线 *remote_folder_path* 

   

2. 函数命名

   一个单词组成: 小写 *test()* 

   多个单词组成: 下划线 *connect_test()* 

   

3. 类命名

   一个单词组成: 首字母大写 *Serve()* 

   多个单词组成: 首字母大写&末尾字母大写 *SoftwareTools()* 

   

4. 文件命名

   一个单词组成: 小写 *remove.py* 

   多个单词组成: 首字母大写&末尾字母大写 *DatabaseTools.py* 

     

5. 文件夹命名

   一个单词组成: 大写 *Temp* 

   多个单词组成: 首字母大写&末尾字母大写 *FileTools* 

   

6.  模块命名

      一个单词组成: 大写 *Serve* 

      多个单词组成: 首字母大写&末尾字母大写 *FileTools* 


7. 类调用

   一个单词组成: 前面两个字母大写 SE = *Serve()*

   多个单词组成: 首字母大写&末尾字母大写 ST = *SoftwareTools()* 


7. 函数出参入参注释
```python
def read_yaml(yml_path = ""):
   """
   文件夹不存在则创建
   :param folder_path: 文件夹地址
   :return: yml文件地址
   """
   return yml_path
```

8. 类初始化函数注释
```python
class YamlCurd(obejct):
   """
   yaml 操作
   """
   def __init__(self):
      pass
   def read_yaml(self,yml_path = ""):
      """
      文件夹不存在则创建
      :param folder_path: 文件夹地址
      :return: yml文件地址
      """
      return yml_path
```


9. 文件要有函数入口测试
```python
class YamlCurd(obejct):
      """
      yaml 操作
      """
      def __init__(self):
         pass
      def read_yaml(self,yml_path = ""):
         """
         文件夹不存在则创建
         :param folder_path: 文件夹地址
         :return: 创建成功
         """
         return yml_path
   
   
if __name__ == '__main__':
   YC = YamlCurd()
   YC.read_yml(F'demo.yml')

```

10. 变量值

      变量值   优先使用双引号 " "
```python
age = 18
name = "小明"
```

11.  格式化字符串f-string
   
      f或者F 优先使用 F + ' '
```python
age = 18
name = "小明"
result  = F'{name}今年{age}岁'
```

12. 转义字符 R或者r

    转义字符 使用优先使用大写 R

    路径类   使用优先使用大写 R
```python
yml_path = R'./yml_path'
```


## 使用说明

1.  导入相关包
```python
from FileTools.YmlTools import YmlCurd
```

2.  初始化
```python
from FileTools.YmlTools import YmlCurd
YC = YmlCurd()
```
3.  使用相关函数
```python
from FileTools.YmlTools import YmlCurd
YC = YmlCurd()
YC.read_yaml()
```

