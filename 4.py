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
url = 'https://wap.showstart.com/pages/order/activity/confirm/confirm?sequence=231189&ticketId=2d73c0dcd9a9a36fba872761af34f071&ticketNum=1'
driver.get(url)

time.sleep(10)

# 注入token
key = 'userInfo'
# 王桂芳
strs = '{"type":"object","data":{"st_flpv":"1f11c35qsr7yz79qq202mhxkj7i1bxuz","userId":15657891,"userType":1,"tuType":0,"userName":"Fan2156578910","avatar":"https://s2.showstart.com/img/2024/0409/09/30/de2d0d57f4d0427ab447dee78fc47306_800_800_661402.0x0.jpg","loginTime":1718285129077,"sign":"bebbf4c95dd859db2bfc89006c0cef1f","ticketWalletServiceStatus":2,"tel":"18553365720","expireTime":1720877129079,"isChoose":1,"areaCode":"86_CN","uniqueCode":"55dc974b99e098560316e0604427379f","imAppId":1400331755,"isRealName":1,"isAdmin":0,"userLevel":3,"memberExpireTime":0,"idtoken":"aaa3a08f14a8ad0e666afb7d7e7d004c","id":15657891,"name":"Fan2156578910","isCollect":0,"creditLevel":0,"creditLevelExp":[20,131,420,1634,4257]}}'
driver.execute_script(f"window.localStorage.setItem('{key}', '{strs}');")
driver.get(url)

time.sleep(60 * 60 *24)