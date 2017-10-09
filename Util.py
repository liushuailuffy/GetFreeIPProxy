import random

import ProxiesDataBaseMysql
import GetIP
import re

def Refresh():
    GetIP.RefreshDB()
    GetIP.GetIP()

def Get():
    proxies_dict = {}
    result = ProxiesDataBaseMysql.GetItems()
    if result:
        tmp = random.choice(result)
        proxies_dict['http:'] = 'http://{}'.format(tmp)
        proxies_dict['https:'] = 'https://{}'.format(tmp)
    return proxies_dict

def Getiplist():
    result1 = ProxiesDataBaseMysql.GetItems()
    return result1
