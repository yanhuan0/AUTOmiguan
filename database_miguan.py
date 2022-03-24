
import requests
import json
import logging
from urllib import parse

logger = logging.getLogger()
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('log.txt', encoding='utf-8')
# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s |%(levelname)s|  %(message)s')
logger.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)  # logger对象可以添加多个fh和ch对象
logger.addHandler(ch)


COOKIE = """session=MTY0NzgyNzk1NnxOd3dBTkZWT1MxcFJXRVJHVjBWWldFbEVRVkZTTTFZMlREZFpWa3RhTkVoTVRFODNVRUpNV0RSR1dGZzBVMUUzUmt3eVVsTktWRUU9fJt8ZaOCQf_s5ycNRsqXwGSZuo8CEm7x6Z4ZY3i0Yvrk; s=zhongwc"""

HEADERS = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://10.19.159.22',
    'Referer': 'https://10.19.159.22/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cookie': COOKIE
}

IP = '10.19.159.22'

HONEYNET_ID = 1

def mysql(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoMysql", "service_id": 1, "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "honeypot_template_id": "" , "ext": json.dumps({"templatSource":"none","retaliationForm":{"open":"false","retaliation_type":1,"file":[],"retaliation_file_type":""},"is_open":"false"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def redis(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoRedis", "service_id": 2, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def elasticsearch(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoES", "service_id": 3, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def memcached(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoMem", "service_id": 4, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def postgreSQL(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoPG", "service_id": 5, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def mongoDB(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoMongoDB", "service_id": 6, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def hbase(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoHBase", "service_id": 7, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def hive(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoHive", "service_id": 8, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def mssql(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoMSsql", "service_id": 29, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def main():
    #mysql()
    #redis()
    #elasticsearch()
    #memcached()
    #postgreSQL()
    #mongoDB()
    #hbase()
    #hive()
    mssql()

if __name__ == "__main__":
    main()
