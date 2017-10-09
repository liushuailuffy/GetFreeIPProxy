
import GetIP
import random
import Config
import ProxiesDataBaseMysql
import Util


def main():
    # 初始化数据库和数据表
    ProxiesDataBaseMysql.InitDB()
    # 刷新数据库，添加新数据
    Util.Refresh()
    # 获取一个代理使用
    proxies = Util.Get()
    print("获取到代理：",proxies)


    
    

if __name__ == '__main__':
    main()
