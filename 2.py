from ast import If
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 设置Chrome浏览器的选项
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # 如果不需要浏览器界面，可启用无头模式
# options.add_argument('--disable-gpu')  # 适用于无头模式

# 初始化webdriver
driver = webdriver.Chrome(options=options)

# 打开指定的URL
url = 'https://wap.showstart.com/pages/order/activity/confirm/confirm?sequence=231189&ticketId=f2543a9ee746e94a481b30956a0a4544&ticketNum=1'
driver.get(url)

time.sleep(10)

# 注入token
key = 'userInfo'
# 小武1
strs = '{"type":"object","data":{"st_flpv":"t8c3hsulwe95m8z488tw2811bsmwvy8a","userId":17632284,"userType":1,"tuType":0,"userName":"Fan6176322840","avatar":"https://s2.showstart.com/img/2024/0412/09/30/799f76d40dff4f0288af5a244e68309d_200_200_19735.0x0.png","loginTime":1718330161730,"sign":"f0bd7bc4f51c92ac23db03215eb9bb27","ticketWalletServiceStatus":0,"tel":"17513319289","expireTime":1720922161732,"isChoose":0,"areaCode":"86_CN","uniqueCode":"067a1769a3ca6d09fd85902ff196a028","imAppId":1400331755,"isRealName":0,"isAdmin":0,"memberExpireTime":0,"idtoken":"cf0df6dec53e3559666bab65e94589c2"}}'
driver.execute_script(f"window.localStorage.setItem('{key}', '{strs}');")
driver.get(url)