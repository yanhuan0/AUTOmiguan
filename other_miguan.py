
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


COOKIE = """session=MTY0ODAyMjE3MXxOd3dBTkVoWlYwWllTRkJETmt0R1JVWlJSa0pOUWtkV1JWbzJNMGxMUmtWRVEwRkdURGRPU1RaVFREYzBWVFpHV2xnMU5Fc3lSVUU9fITVz0CAhiC0dLjsmhT7xYuMWzdsejxuyQRHc3yMGzNv; s=zhongwc"""

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

def ssh(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoSSH", "service_id": 21, "honeypot_type": 2, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert","template_name":"","user":"root","hostname":"autotest","passwd":"123456"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def telnet(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoTelnet", "service_id": 22, "honeypot_template_id": "null", "honeypot_type": 1,  "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})} 
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def eternalBlue(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoEBlue", "service_id": 23, "honeypot_template_id": "null", "honeypot_type": 1,  "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def ftp(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoFTP", "service_id": 24, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def smb(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoSMB", "service_id": 38, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def modbus(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoModbus", "service_id": 44, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def iec104(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoIEC104", "service_id": 45, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def iec61850(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "Auto61850", "service_id": 46, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def s7(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoS7", "service_id": 47, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def opc(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoIEC104", "service_id": 48, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def main():
    ssh()
    telnet()
    eternalBlue()
    ftp()
    smb()
    modbus()
    iec104()
    iec61850()
    s7()
    opc()

if __name__ == "__main__":
    main()
