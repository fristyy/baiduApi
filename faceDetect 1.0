#coding:utf-8

import sys,urllib
from urllib import request
import ssl
from collections.abc import Mapping,MutableSequence
import base64
import json

# client_id 为官网获取的AK， client_secret 为官网获取的SK
def ac_token():
	host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=ZFHT0eNCmjvMcdsKpnDPtMtn&client_secret=[自己的key]'
	req = request.Request(host)
	req.add_header('Content-Type', 'application/json; charset=UTF-8')
	resp = request.urlopen(req)
	content = resp.read().decode('utf-8')
	if (content):
		print(content)
		try:
			dic = json.loads(content)
			return dic 
		except Exception as e:
			print('获取参数错误',e)
			
#已获得以下token, 有效期30天,当前获取日期1月15日			
access_token = '24.e80d12bcd638f0ef4403d0532eaebcd5.2592000.1550125674.282335-15422738'

#图片转换
def tranBase64(imgpath):
	with open(imgpath, 'rb') as f:
		base64_base = base64.b64encode(f.read())
		s = base64_base.decode()
		print(f'base64数据长度{len(s)}字节')
		if len(s)>2000000:
			raise FError('base64字节太长了')
		return s

#人脸识别接口请求
#HTTP方法：POST
#请求URL： https://aip.baidubce.com/rest/2.0/face/v3/detect

#人脸对比接口请求
#HTTP方法：POST
#请求URL： https://aip.baidubce.com/rest/2.0/face/v3/match

#用于解析返回结果
def dicParse(dic):
	for key in dic:
		if isinstance(dic[key],dict):
			dicParse(dic[key])
		elif isinstance(dic[key],MutableSequence):
			for elem in dic[key]:
				dicParse(elem)			
		else:
			print(key,':',dic[key])

#调用人脸检测API
def faceDetec(img,img_type):
	request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
	
	params = {"image":img,"image_type":img_type,"face_field":"age,beauty,expression,gender,emotion"}
	params = urllib.parse.urlencode(params).encode(encoding='UTF8')
	request_url = request_url + "?access_token=" + access_token
	req =request.Request(url=request_url, data=params)
	req.add_header('Content-Type', 'application/json')
	resp = request.urlopen(req)
	content = resp.read().decode('utf-8')
	if content:
		#print(content)
		return content


#人脸比对
def faceMatch(jsonData):
	request_url = 'https://aip.baidubce.com/rest/2.0/face/v3/match'
	
	params = json.dumps(jsonData).encode()
	#params = urllib.parse.urlencode(jsonData).encode(encoding='UTF8')
	request_url = request_url + "?access_token=" + access_token
	req =request.Request(url=request_url, data=params)
	req.add_header('Content-Type', 'application/json')
	resp = request.urlopen(req)
	content = resp.read().decode('utf-8')
	if content:
		#print(content)
		return content	
	

def resultsPares(results):
	results = json.loads(results)
	if isinstance(results,dict):
		dicParse(results)
	else:
		print(results)

def main():		

	#img_base64 = tranBase64("E:/baiduyunApi/factDetect/15c.jpg")
	#image_type:BASE64,URL,FACE_TOKEN  face_token在使用base64进行一次检测后生成	
	
	'''人脸检测调用'''
	#results = faceDetec(img_base64,"BASE64")
	
	'''人脸对比调用'''
	#img2_base64 = tranBase64("E:/baiduyunApi/factDetect/12c.jpg")
	jsonData = [{
        "image": '6c9edf350d789723f02088a49ff9fd49',
        "image_type": "FACE_TOKEN",
        "face_type": "LIVE",
    },
    {
        "image": 'ea49821039bf8effdca0e59264e1e06b',
        "image_type": "FACE_TOKEN",
        "face_type": "LIVE",
    }]
	results = faceMatch(jsonData)
	
	resultsPares(results)

if __name__ == '__main__':
	main()
	


#http://ai.baidu.com/docs#/Face-Match-V3/top
#以下部分为示例	
#人脸比对json参数示例
	'''[
    {
        "image": "sfasq35sadvsvqwr5q...",
        "image_type": "BASE64",
        "face_type": "LIVE",
        "quality_control": "LOW",
        "liveness_control": "HIGH"
    },
    {
        "image": "sfasq35sadvsvqwr5q...",
        "image_type": "BASE64",
        "face_type": "IDCARD",
        "quality_control": "LOW",
        "liveness_control": "HIGH"
    }
]'''

#返回数据说明
'''字段	必选	类型	说明
face_num	是	int	检测到的图片中的人脸数量
face_list	是	array	人脸信息列表，具体包含的参数参考下面的列表。
+face_token	是	string	人脸图片的唯一标识
+location	是	array	人脸在图片中的位置
++left	是	double	人脸区域离左边界的距离
++top	是	double	人脸区域离上边界的距离
++width	是	double	人脸区域的宽度
++height	是	double	人脸区域的高度
++rotation	是	int64	人脸框相对于竖直方向的顺时针旋转角，[-180,180]
+face_probability	是	double	人脸置信度，范围【0~1】，代表这是一张人脸的概率，0最小、1最大。
+angel	是	array	人脸旋转角度参数
++yaw	是	double	三维旋转之左右旋转角[-90(左), 90(右)]
++pitch	是	double	三维旋转之俯仰角度[-90(上), 90(下)]
++roll	是	double	平面内旋转角[-180(逆时针), 180(顺时针)]
+age	否	double	年龄 ，当face_field包含age时返回
+beauty	否	int64	美丑打分，范围0-100，越大表示越美。当face_fields包含beauty时返回
+expression	否	array	表情，当 face_field包含expression时返回
++type	否	string	none:不笑；smile:微笑；laugh:大笑
++probability	否	double	表情置信度，范围【0~1】，0最小、1最大。
+face_shape	否	array	脸型，当face_field包含face_shape时返回
++type	否	double	square: 正方形 triangle:三角形 oval: 椭圆 heart: 心形 round: 圆形
++probability	否	double	置信度，范围【0~1】，代表这是人脸形状判断正确的概率，0最小、1最大。
+gender	否	array	性别，face_field包含gender时返回
++type	否	string	male:男性 female:女性
++probability	否	double	性别置信度，范围【0~1】，0代表概率最小、1代表最大。
+glasses	否	array	是否带眼镜，face_field包含glasses时返回
++type	否	string	none:无眼镜，common:普通眼镜，sun:墨镜
++probability	否	double	眼镜置信度，范围【0~1】，0代表概率最小、1代表最大。
+eye_status	否	array	双眼状态（睁开/闭合） face_field包含eye_status时返回
++left_eye	否	double	左眼状态 [0,1]取值，越接近0闭合的可能性越大
++right_eye	否	double	右眼状态 [0,1]取值，越接近0闭合的可能性越大
+emotion	否	array	情绪 face_field包含emotion时返回
++type	否	string	angry:愤怒 disgust:厌恶 fear:恐惧 happy:高兴
sad:伤心 surprise:惊讶 neutral:无情绪
++probability	否	double	情绪置信度，范围0~1
+race	否	array	人种 face_field包含race时返回
++type	否	string	yellow: 黄种人 white: 白种人 black:黑种人 arabs: 阿拉伯人
++probability	否	double	人种置信度，范围【0~1】，0代表概率最小、1代表最大。
+face_type	否	array	真实人脸/卡通人脸 face_field包含face_type时返回
++type	否	string	human: 真实人脸 cartoon: 卡通人脸
++probability	否	double	人脸类型判断正确的置信度，范围【0~1】，0代表概率最小、1代表最大。
+landmark	否	array	4个关键点位置，左眼中心、右眼中心、鼻尖、嘴中心。face_field包含landmark时返回
+landmark72	否	array	72个特征点位置 face_field包含landmark时返回
+quality	否	array	人脸质量信息。face_field包含quality时返回
++occlusion	否	array	人脸各部分遮挡的概率，范围[0~1]，0表示完整，1表示不完整
+++left_eye	否	double	左眼遮挡比例，[0-1] ，1表示完全遮挡
+++right_eye	否	double	右眼遮挡比例，[0-1] ， 1表示完全遮挡
+++nose	否	double	鼻子遮挡比例，[0-1] ， 1表示完全遮挡
+++mouth	否	double	嘴巴遮挡比例，[0-1] ， 1表示完全遮挡
+++left_cheek	否	double	左脸颊遮挡比例，[0-1] ， 1表示完全遮挡
+++right_cheek	否	double	右脸颊遮挡比例，[0-1] ， 1表示完全遮挡
+++chin	否	double	下巴遮挡比例，，[0-1] ， 1表示完全遮挡
++blur	否	double	人脸模糊程度，范围[0~1]，0表示清晰，1表示模糊
++illumination	否	double	取值范围在[0~255], 表示脸部区域的光照程度 越大表示光照越好
++completeness	否	int64	人脸完整度，0或1, 0为人脸溢出图像边界，1为人脸都在图像边界内'''
