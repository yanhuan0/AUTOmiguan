
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

IP = '10.19.159.22'

HONEYNET_ID= 1

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


def weblogic(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoWeblogic", "service_id": 9, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def struts2(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoStruts2", "service_id": 10, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def thinkphp(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoThinkphp", "service_id": 11, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def tomcat(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoTomcat", "service_id": 12, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def shellshock(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoShellshock", "service_id": 13, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def phpupload(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoPhpupload", "service_id": 14, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def nexus(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoNexus", "service_id": 15, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def jboss(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoJboss", "service_id": 16, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def sqlinject(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoInject", "service_id": 17, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)


def zidingyi(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoZidingYi", "service_id": 25, "honeypot_type": 2, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"template_name":"","type":2,"url":"https://www.asiainfo.com/zh_cn/index.html","replace":1})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def ciscoVPN(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoCVPN", "service_id": 26, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext":  json.dumps({"templatSource":"insert","retaliationForm":{"open":"false","retaliation_type":1,"file":[],"retaliation_file_type":""}})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def mmwiki():
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoWiki", "service_id": 27, "honeynet_id": HONEYNET_ID, "honeypot_type": 2, "ext": json.dumps({"templatSource":"insert","template_name":"","ssl_file":[],"ssl_type":1,"company":"company","title":"title","description":"description","admin_password":"123456","retaliationForm":{"open":"false","retaliation_type":1,"file":[],"retaliation_file_type":""}})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def ranzhi():
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoRZ", "service_id": 28, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "retaliation_type": 1, "ext": json.dumps({"templatSource":"none","retaliationForm":{"open":"false","retaliation_type":1,"file":[],"retaliation_file_type":""}})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def sslvpn():
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoSSLVPN", "service_id": 30, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"none","retaliationForm":{"open":"false","retaliation_type":1,"file":[],"retaliation_file_type":""}})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def discuz(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoDiscuz", "service_id": 31, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"none"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def jenkins(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoJenkins", "service_id": 32, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"none"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def turboMail(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoTMail", "service_id": 33, "honeypot_type": 2, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert","template_name":"","ssl_file":[],"ssl_type":1,"company":"turbomail","domain_name":"TB"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)


def vtiger(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoVtiger", "service_id": 34, "honeypot_template_id": "null", "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def zabbix(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoZabbix", "service_id": 35, "honeypot_type": 2, "honeynet_id": HONEYNET_ID, "ext":json.dumps({"templatSource":"insert","template_name":"","password":"zabbix"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def redmine(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoRedmine", "service_id": 39, "honeypot_type": 2, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert","template_name":"","ssl_file":[],"ssl_type":1,"company":"AutoRedmine","username":"AutoRedmine","password":"AutoRedmine","retaliationForm":{"open":"false","retaliation_type":1,"file":[],"retaliation_file_type":""}})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def ruoyi(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoRuoyi", "service_id": 38, "honeypot_type": 2, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert","template_name":"","username":"ruoyi","password":"ruoyi"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def joomla(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoJoomla", "service_id": 40, "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def webmin(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoWebmin", "service_id": 41, "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def wordpress(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoWpress", "service_id": 42, "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def fastjson(): 
    url = 'https://' + IP + '/honeypots/'
    Formdata = {"name": "AutoFastjson", "service_id": 43, "honeypot_type": 1, "honeynet_id": HONEYNET_ID, "ext": json.dumps({"templatSource":"insert"})}
    data = parse.urlencode(Formdata)
    resp = requests.post(url, data=data, headers=HEADERS, verify=False)
    logger.info(resp.text)

def main():
    weblogic()
    struts2()
    thinkphp()
    tomcat()
    shellshock()
    phpupload()
    nexus()
    jboss()
    sqlinject()
    zidingyi()  
    ciscoVPN() 
    mmwiki()
    ranzhi()
    sslvpn()
    discuz()
    jenkins()
    turboMail()
    vtiger()
    zabbix()
    redmine()
    ruoyi()
    joomla()
    webmin()
    wordpress()
    fastjson()


if __name__ == "__main__":
    main()
