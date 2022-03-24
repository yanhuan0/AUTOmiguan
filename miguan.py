

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

def syn_bind(agent_id, ip):
    url = f'http://{IP}/agents/{ agent_id }/forwards'
    data_json = {"forward_type": 4, "service_id": "null",
                 "local_port": "1-65535", "local_host": ip}
    resp = requests.post(url, data=json.dumps(data_json), headers=HEADERS)
    logger.info(resp.text)


def udp_bind(agent_id, ip):
    url = f'http://{IP}/agents/{ agent_id }/forwards'
    data_json = {"forward_type": 3, "service_id": "null",
                 "local_port": "100-65535", "local_host": ip}
    resp = requests.post(url, data=json.dumps(data_json), headers=HEADERS)
    logger.info(resp.text)


def icmp_bind(agent_id, ip):
    url = f'http://{IP}/agents/{ agent_id }/forwards'
    data_json = {"forward_type": 5, "service_id": "null",
                 "local_port": None, "local_host": ip}
    resp = requests.post(url, data=json.dumps(data_json), headers=HEADERS)
    logger.info(resp.text)


def tcp_bind(agent_id, ip):
    url = f'http://{IP}/agents/{ agent_id }/forwards'
    data_json = {"forward_type": 2, "service_id": "null",
                 "local_port": "34000-35000", "local_host": ip}
    resp = requests.post(url, data=json.dumps(data_json), headers=HEADERS)
    logger.info(resp.text)


def null_bind(agent_id, ip):
    url = f'http://{IP}/agents/{ agent_id }/forwards'
    data_json = {"forward_type": 6, "service_id": "null",
                 "local_port": "34000-35000", "local_host": ip}
    resp = requests.post(url, data=json.dumps(data_json), headers=HEADERS)
    logger.info(resp.text)


def xmas_bind(agent_id, ip):
    url = f'http://{IP}/agents/{ agent_id }/forwards'
    data_json = {"forward_type": 7, "service_id": "null",
                 "local_port": "34000-35000", "local_host": ip}
    resp = requests.post(url, data=json.dumps(data_json), headers=HEADERS)
    logger.info(resp.text)

def honeypot_bind(agent_id,ip):
    url = f'http://{IP}/agents/{ agent_id }/forwards'
    port = 9000
    for potid in range(1,10,1):
        port += 1
        data_json = {"forward_type":1,"local_port":str(port),"local_host":ip,"honeynet_id":1,"honeypot_id":potid}
        print(data_json)
        resp = requests.post(url, data=json.dumps(data_json), headers=HEADERS)
        logger.info(resp.text)

def get_agents():
    url = f'https://{IP}/agents/?page=1&page_size=300'
    resp = requests.get(url, headers=HEADERS, verify=False)
    if resp.status_code == 200:
        logger.info(resp.json()["total"])
        return resp.json()["data"]["list"]
    else:
        logger.error("请求失败")
        return []


def main():
    # syn_bind("e867018fe3a00abd", "192.168.122.149")

    agents = get_agents()
    for agent in agents:
        logger.info(agent["agentID"] + " " +
                    agent["localIP"] + "\t " + agent["status_str"])
        if agent["status_str"] == "在线":
            syn_bind(agent["agentID"],agent["localIP"])
            udp_bind(agent["agentID"],agent["localIP"])
            icmp_bind(agent["agentID"],agent["localIP"])
            tcp_bind(agent["agentID"], agent["localIP"])
            null_bind(agent["agentID"],agent["localIP"])
            xmas_bind(agent["agentID"], agent["localIP"])
            #honeypot_bind(agent["agentID"], agent["localIP"])


if __name__ == "__main__":
    main()
