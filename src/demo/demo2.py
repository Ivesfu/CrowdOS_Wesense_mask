# -*- coding: utf-8 -*-
# 2021/9/17 fyh
import urllib.request
import urllib.error
import time
import os
import json

http_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
key = "IbD5_-h16Ix-r8MH5Ug5UeUi0qQBlRX-"
secret = "lJTYKB1LitUv0bBFnYehW_NcJy_MYRF3"
mask = 0
tot = 0
headers = {'User-Agent':'Mozilla/5.0 3578.98 Safari/537.36'}

def getinfo(filepath): # 识别图片并统计信息
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
    fr = open(filepath, 'rb')
    data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
    data.append('Content-Type: %s\r\n' % 'application/octet-stream')
    data.append(fr.read())
    fr.close()
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_landmark')
    data.append('1')
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_attributes')
    data.append(
        "gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,skinstatus")
    data.append('--%s--\r\n' % boundary)

    for i, d in enumerate(data):
        if isinstance(d, str):
            data[i] = d.encode('utf-8')

    http_body = b'\r\n'.join(data)
    req = urllib.request.Request(url=http_url, data=http_body, headers=headers)
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
    resp = urllib.request.urlopen(req, timeout=15)
    qrcont = resp.read()
    st = qrcont.decode('utf-8')
    lst = json.loads(st)

    n = len(lst['faces']) # 识别出来的人数n

    global tot
    tot = tot + n

    # print("照片上的人数大约有%d人"%(n))
    cnt = 0 # 带口罩的人数
    for i in range(n):
        if i >= 5 : break
        if lst['faces'][i]["attributes"]["mouthstatus"]["surgical_mask_or_respirator"] > 13.0 :
            cnt = cnt + 1
    global mask
    mask = mask + cnt

dict = {}


# 1a----------------------------------------------------------------- 
tot = 0
mask = 0
path = "./testphotos/airport"
files = os.listdir(path)   # 读入文件夹
num_jpg = len(files)       # 统计文件夹中的文件个数
for i in range(num_jpg):
    filepath = r"./testphotos/airport/" 
    filepath += "a (%d).jpg"%(i + 1)
    getinfo(filepath)
    time.sleep(0.5)

print("机场场合数据集, 共识别了%d人, 带口罩的比例：%f"%(tot,mask / tot))
dict[0] = []
dict[0].append(tot)
dict[0].append(mask)
dict[0].append(mask / tot)
dict[0].append("机场场合")


# 2b----------------------------------------------------------------- 
tot = 0
mask = 0
path = "./testphotos/train_station"
files = os.listdir(path)   
num_jpg = len(files)       
for i in range(num_jpg):
    filepath = r"./testphotos/train_station/"
    filepath += "b (%d).jpg"%(i + 1)
    getinfo(filepath)
    time.sleep(0.5)

print("火车站场合数据集, 共识别了%d人, 带口罩的比例：%f"%(tot,mask / tot))
dict[1] = []
dict[1].append(tot)
dict[1].append(mask)
dict[1].append(mask / tot)
dict[1].append("火车站场合")


# 3c----------------------------------------------------------------- 
tot = 0
mask = 0
path = "./testphotos/park"
files = os.listdir(path)   
num_jpg = len(files)     
for i in range(num_jpg):
    filepath = r"./testphotos/park/"
    filepath += "c (%d).jpg"%(i + 1)
    getinfo(filepath)
    time.sleep(0.5)

print("公园社区场合数据集, 共识别了%d人, 带口罩的比例：%f"%(tot,mask / tot))
dict[2] = []
dict[2].append(tot)
dict[2].append(mask)
dict[2].append(mask / tot)
dict[2].append("公园社区场合")


# 4d----------------------------------------------------------------- 
tot = 0
mask = 0
path = "./testphotos/market"
files = os.listdir(path)   
num_jpg = len(files)     
for i in range(num_jpg):
    filepath = r"./testphotos/market/"
    filepath += "d (%d).jpg"%(i + 1)
    getinfo(filepath)
    time.sleep(0.5)

print("商场场合数据集, 共识别了%d人, 带口罩的比例：%f"%(tot,mask / tot))
dict[3] = []
dict[3].append(tot)
dict[3].append(mask)
dict[3].append(mask / tot)
dict[3].append("商场场合")


# 5e----------------------------------------------------------------- 
tot = 0
mask = 0
path = "./testphotos/scenic"
files = os.listdir(path)   
num_jpg = len(files)     
for i in range(num_jpg):
    filepath = r"./testphotos/scenic/"
    filepath += "e (%d).jpg"%(i + 1)
    getinfo(filepath)
    time.sleep(0.5)

print("景区数据集, 共识别了%d人, 带口罩的比例：%f"%(tot,mask / tot))
dict[4] = []
dict[4].append(tot)
dict[4].append(mask)
dict[4].append(mask / tot)
dict[4].append("景区场合")


# 6f----------------------------------------------------------------- 
tot = 0
mask = 0
path = "./testphotos/school"
files = os.listdir(path)   
num_jpg = len(files)     
for i in range(num_jpg):
    filepath = r"./testphotos/school/"
    filepath += "f (%d).jpg"%(i + 1)
    getinfo(filepath)
    time.sleep(0.5)

print("学校场合数据集, 共识别了%d人, 带口罩的比例：%f"%(tot,mask / tot))
dict[5] = []
dict[5].append(tot)
dict[5].append(mask)
dict[5].append(mask / tot)
dict[5].append("学校场合")


# 7g----------------------------------------------------------------- 
tot = 0
mask = 0
path = "./testphotos/hospital"
files = os.listdir(path)   
num_jpg = len(files)     
for i in range(num_jpg):
    filepath = r"./testphotos/hospital/"
    filepath += "g (%d).jpg"%(i + 1)
    getinfo(filepath)
    time.sleep(0.5)

print("医院场合数据集, 共识别了%d人, 带口罩的比例：%f"%(tot,mask / tot))
dict[6] = []
dict[6].append(tot)
dict[6].append(mask)
dict[6].append(mask / tot)
dict[6].append("医院场合")


# 8h----------------------------------------------------------------- 
tot = 0
mask = 0
path = "./testphotos/America"
files = os.listdir(path)   
num_jpg = len(files)     
for i in range(num_jpg):
    filepath = r"./testphotos/America/"
    filepath += "h (%d).jpg"%(i + 1)
    getinfo(filepath)
    time.sleep(0.5)

print("America数据集, 共识别了%d人, 带口罩的比例：%f"%(tot,mask / tot))
dict[7] = []
dict[7].append(tot)
dict[7].append(mask)
dict[7].append(mask / tot)
dict[7].append("America场合")


# 9i----------------------------------------------------------------- 
tot = 0
mask = 0
path = "./testphotos/foreign"
files = os.listdir(path)   
num_jpg = len(files)     
for i in range(num_jpg):
    filepath = r"./testphotos/foreign/"
    filepath += "I (%d).jpg"%(i + 1)
    getinfo(filepath)
    time.sleep(0.5)

print("国外数据集, 共识别了%d人, 带口罩的比例：%f"%(tot,mask / tot))
dict[8] = []
dict[8].append(tot)
dict[8].append(mask)
dict[8].append(mask / tot)
dict[8].append("外国场合")


# 10j---------------------------------------------------------------- 
tot = 0
mask = 0
path = "./testphotos/school_foreign"
files = os.listdir(path)   
num_jpg = len(files)     
for i in range(num_jpg):
    filepath = r"./testphotos/school_foreign/"
    filepath += "j (%d).jpg"%(i + 1)
    getinfo(filepath)
    time.sleep(0.5)

print("外国学校数据集, 共识别了%d人, 带口罩的比例：%f"%(tot,mask / tot))
dict[9] = []
dict[9].append(tot)
dict[9].append(mask)
dict[9].append(mask / tot)
dict[9].append("外国学校场合")


# 11k----------------------------------------------------------------
tot = 0
mask = 0
path = "./testphotos/hospital_foreign"
files = os.listdir(path)   
num_jpg = len(files)     
for i in range(num_jpg):
    filepath = r"./testphotos/hospital_foreign/"
    filepath += "k (%d).jpg"%(i + 1)
    getinfo(filepath)
    time.sleep(0.5)

print("国外医院集, 共识别了%d人, 带口罩的比例：%f"%(tot,mask / tot))
dict[10] = []
dict[10].append(tot)
dict[10].append(mask)
dict[10].append(mask / tot)
dict[10].append("外国医院场合")


f = open('./visweb/tmp.json', 'w')
b = json.dumps(dict)
f.write(b)
f.close()