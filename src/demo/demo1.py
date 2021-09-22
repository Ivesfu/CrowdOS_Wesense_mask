# -*- coding: utf-8 -*-
# 2021/9/14 fyh
import urllib.request
import urllib.error
import time
import json

http_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
key = "IbD5_-h16Ix-r8MH5Ug5UeUi0qQBlRX-"
secret = "lJTYKB1LitUv0bBFnYehW_NcJy_MYRF3"
filepath = r"./testphotos/test009.jpg"

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
req = urllib.request.Request(url=http_url, data=http_body)
req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
resp = urllib.request.urlopen(req, timeout=5)
qrcont = resp.read()
str = qrcont.decode('utf-8')
lst = json.loads(str)

n = len(lst['faces']) # 识别出来的人数n
print("照片上的人数大约有%d人"%(n))
cnt = 0 # 没带口罩的人数
for i in range(n):
    if i >= 5 : break
    if lst['faces'][i]["attributes"]["mouthstatus"]["surgical_mask_or_respirator"] > 13.0 :
        cnt = cnt + 1

print("戴口罩的人数大约有%d人"%(cnt))