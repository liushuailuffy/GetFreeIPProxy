# GetFreeIPProxy
获取免费的的IP代理，抓取八个网站的代理IP检测/清洗/入库/更新，添加调用接口<br>
数据库为mysql
目前只在<strong>win10 64位机，python3.5</strong> 下测试通过<br>

<hr /><br>

<h3>如何使用</h3>
查看<a href="https://github.com/liushuailuffy/GetFreeIPProxy/blob/master/start.py">start.py</a><br><br>
Util.Refresh()：刷新数据库，并获取新的代理IP<br><br>
Util.Get()：返回可获取一条可用的代理，Util.Get()返回的代理：<br>
{'http': 'http://115.159.152.111:91', 'https': 'https://115.159.152.111:91'}<br>
requests可以直接使用：requests.get(url,proxies=Util.Get(),headers={})
<hr /><br>

<h3>Config.py 部分：</h3>
<strong>设置最大线程数量限制</strong>，MaxThreads。<br>
<strong>如果你还有代理网站可以添加</strong>，请添加在Url_Regular字典中。<br>
代理IP网址和对应的正则式，<strong>正则式一定要IP和Port分开获取</strong>，例如[(192.168.1.1, 80), (192.168.1.1, 90),]<br>
只抓取首页，<strong>想要抓取首页以后页面的可以将链接和正则式贴上来</strong>，例如，将某网站的1、2、……页的链接和对应的正则式分别添加到Url_Regular字典中。<br>
<strong>添加正则式之前</strong>请先在 <a href="http://tool.chinaz.com/regex">站长工具-正则表达式在线测试</a> 测试通过后添加<br>
<hr /><br>
<strong>欢迎添加你知道的代理网站，大家资源共享</strong>
<hr /><br>
