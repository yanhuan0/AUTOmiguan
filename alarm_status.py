
import sys
import requests
import json
import logging

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
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://10.19.159.22',
    'Referer': 'https://10.19.159.22/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cookie': COOKIE
}


IP = '10.19.159.22'

def honeypot_bind(aids):
    url = f'http://{IP}/attack_alarm_fun/batch_status'
    data_json = {"ids":[ aids ],"status":2}

    
    resp = requests.put(url, data=json.dumps(data_json), headers=HEADERS, verify=False)
    logger.info(resp.text)

def get_alarmsid():
    url = f'https://{IP}/attack_alarms/?page=1&condition[status]=0&page_size=1000'
    resp = requests.get(url, headers=HEADERS, verify=False)
    if resp.status_code == 200:
        logger.info(resp.json()["total"])
        return resp.json()["data"]
    else:
        logger.error("请求失败")
        return []


def main():

    alarmsid = get_alarmsid()
    for aids in alarmsid:
        logger.info(aids["ID"])
        honeypot_bind(aids["ID"])


if __name__ == "__main__":
    main()
