from ast import If
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 设置Chrome浏览器的选项
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')  # 如果不需要浏览器界面，可启用无头模式
options.add_argument("--window-size=1920,1080")
options.add_argument('--disable-gpu')  # 适用于无头模式

# 初始化webdriver
driver = webdriver.Chrome(options=options)

# 打开指定的URL
url = 'https://wap.showstart.com/pages/order/activity/confirm/confirm?sequence=231189&ticketId=2d73c0dcd9a9a36fba872761af34f071&ticketNum=1'
driver.get(url)
# 等待10s加载完成
time.sleep(10)

# 注入token
key = 'userInfo'
strs = '{"type":"object","data":{"st_flpv":"7to5tu4mo9ajk59u1lt1jzn8effohqqs","userId":14507810,"userType":1,"tuType":0,"userName":"Fan1145078100","avatar":"https://s2.showstart.com/img/2024/0412/09/30/3ef4e1f431884ee6b4896dcf1a41407a_200_200_16557.0x0.png","loginTime":1718284815785,"sign":"43c4b9e73a68c00f1ec7372d145a61b3","ticketWalletServiceStatus":2,"tel":"18661716316","expireTime":1720876815787,"isChoose":1,"areaCode":"86_CN","uniqueCode":"dc41fd1680bdb009ef57be048a2e70a8","imAppId":1400331755,"isRealName":1,"isAdmin":0,"userLevel":3,"memberExpireTime":0,"idtoken":"7a2a5ee54a99eeff666afa43213b263e","id":14507810,"name":"Fan1145078100","isCollect":0,"creditLevel":0,"creditLevelExp":[20,131,420,1634,4257]}}'
driver.execute_script(f"window.localStorage.setItem('{key}', '{strs}');")
driver.get(url)

# 打印userInfo 确认成功
script = "return window.localStorage.getItem('userInfo');"
value = driver.execute_script(script)
print(value)
# 等待10s加载完成
time.sleep(10)
# 打开观演人
driver.find_elements(By.CLASS_NAME, "rr")[0].click()
time.sleep(1)
# 选择观演人
driver.find_elements(By.CLASS_NAME, "uni-checkbox-input")[0].click()
time.sleep(1)
# 点击确定按钮
confirm_button = driver.find_element(By.XPATH, '//uni-view[contains(text(), "确定")]')
confirm_button.click()

time.sleep(10)
pay_btn = driver.find_elements(By.CLASS_NAME, "payBtn")[0]

# 定义确认方法
def start():
    while True:
      pay_btn.click()
      print('点击了')
      print(driver.execute_script(get_time_script))
      time.sleep(2)

# 获取浏览器当前时间的 JavaScript 脚本
get_time_script = "return new Date().getHours() + ':' + new Date().getMinutes() + ':' + new Date().getSeconds();"
try:
    # 循环获取并打印浏览器的当前时间
    while True:
        current_time = driver.execute_script(get_time_script)
        seconds = current_time.split(':')[2]
        minutes = current_time.split(':')[1]
        hours = current_time.split(':')[0]
        print(f"{hours}时{minutes}分{seconds}秒")
        if minutes == '0':
            start()
            break
        time.sleep(0.001)  # 每0.001秒获取一次
finally:
    current_time = driver.execute_script(get_time_script)



