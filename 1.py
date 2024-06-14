from ast import If
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 设置Chrome浏览器的选项
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
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
# 老邢
strs = '{"type":"object","data":{"st_flpv":"7hx55si2aivdu4vf5iwcrxqu1r1nepa9","userId":17630160,"userType":1,"tuType":0,"userName":"Fan6176301600","avatar":"https://s2.showstart.com/img/2024/0412/09/30/799f76d40dff4f0288af5a244e68309d_200_200_19735.0x0.png","loginTime":1718329153847,"sign":"859573f8112c6c38f560befb91904bc6","ticketWalletServiceStatus":0,"tel":"13569679629","expireTime":1720921153847,"isChoose":0,"areaCode":"86_CN","uniqueCode":"39f3754ab81f1c123e98ba42416715d3","imAppId":1400331755,"isRealName":1,"isAdmin":0,"memberExpireTime":0,"idtoken":"5e8d8d632041b405666ba775c2556d5c","id":17630160,"name":"Fan6176301600","isCollect":0,"userLevel":2,"creditLevel":0,"creditLevelExp":[20,131,420,1634,4257]}}'
driver.execute_script(f"window.localStorage.setItem('{key}', '{strs}');")
driver.get(url)

time.sleep(60 * 60 *24)