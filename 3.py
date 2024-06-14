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
# 小武2

strs = '{"type":"object","data":{"st_flpv":"y843oymi5sfwpxp1jm9bw2ra53e35j30","userId":17633217,"userType":1,"tuType":0,"userName":"Fan6176332170","avatar":"https://s2.showstart.com/img/2024/0412/09/30/d5398f9b27374011b06dd4b77baa2b88_200_200_13964.0x0.png","loginTime":1718330307229,"sign":"b0415784dbf77dcc8b6e797e7789ab2d","ticketWalletServiceStatus":0,"tel":"13080131551","expireTime":1720922307229,"isChoose":0,"areaCode":"86_CN","uniqueCode":"4a92f1d3eed179eca49185d1f57d967e","imAppId":1400331755,"isRealName":0,"isAdmin":0,"memberExpireTime":0,"idtoken":"fb3cd6b6f7540418666babf719ca4a44"}}'
driver.execute_script(f"window.localStorage.setItem('{key}', '{strs}');")
driver.get(url)

time.sleep(60 * 60 *24)