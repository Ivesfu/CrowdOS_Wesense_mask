## 后端部分

demo目录是前端部分

后端使用python语言对数据进行处理和分析，使用了flask框架封装api。

测试数据在文件夹testphotos下，里面对应的不同文件夹为收集的不同的场景的图片。

命名格式为test00*.jpg图片为前期测试图片，无需理会。

demo2.py用来统计分析单张图片的情况，图片存放路径依然为testphotos。

通过执行demo2.py 来处理数据集，统计数据，并将结果写入visweb的 tmp.json文件。

执行app.py将tmp.json文件以api形式返回，方便在前端调用，api接口为：http://8.130.172.72:8080/api/demo/ 。



**注意**：不保证未来何时本人会关闭该服务器。                        



----2021/9/20 fyh

