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
# 等待10s加载完成
time.sleep(10)

# 注入token
key = 'userInfo'
# 王桂芳
# '{"type":"object","data":{"st_flpv":"1f11c35qsr7yz79qq202mhxkj7i1bxuz","userId":15657891,"userType":1,"tuType":0,"userName":"Fan2156578910","avatar":"https://s2.showstart.com/img/2024/0409/09/30/de2d0d57f4d0427ab447dee78fc47306_800_800_661402.0x0.jpg","loginTime":1718285129077,"sign":"bebbf4c95dd859db2bfc89006c0cef1f","ticketWalletServiceStatus":2,"tel":"18553365720","expireTime":1720877129079,"isChoose":1,"areaCode":"86_CN","uniqueCode":"55dc974b99e098560316e0604427379f","imAppId":1400331755,"isRealName":1,"isAdmin":0,"userLevel":3,"memberExpireTime":0,"idtoken":"aaa3a08f14a8ad0e666afb7d7e7d004c","id":15657891,"name":"Fan2156578910","isCollect":0,"creditLevel":0,"creditLevelExp":[20,131,420,1634,4257]}}'
# 赵云鹏1
# '{"type":"object","data":{"st_flpv":"7to5tu4mo9ajk59u1lt1jzn8effohqqs","userId":14507810,"userType":1,"tuType":0,"userName":"Fan1145078100","avatar":"https://s2.showstart.com/img/2024/0412/09/30/3ef4e1f431884ee6b4896dcf1a41407a_200_200_16557.0x0.png","loginTime":1718284815785,"sign":"43c4b9e73a68c00f1ec7372d145a61b3","ticketWalletServiceStatus":2,"tel":"18661716316","expireTime":1720876815787,"isChoose":1,"areaCode":"86_CN","uniqueCode":"dc41fd1680bdb009ef57be048a2e70a8","imAppId":1400331755,"isRealName":1,"isAdmin":0,"userLevel":3,"memberExpireTime":0,"idtoken":"7a2a5ee54a99eeff666afa43213b263e","id":14507810,"name":"Fan1145078100","isCollect":0,"creditLevel":0,"creditLevelExp":[20,131,420,1634,4257]}}'
# 真武
# strs = '{"type":"object","data":{"st_flpv":"bj2e455xo3xjxczd8ny1cozh2s5p3skf","userId":15654053,"userType":1,"tuType":0,"userName":"Fan2156540530","avatar":"https://s2.showstart.com/img/2024/0412/09/30/3ef4e1f431884ee6b4896dcf1a41407a_200_200_16557.0x0.png","loginTime":1718286173554,"sign":"206c949bb78ec48207b620c16c9f0d70","ticketWalletServiceStatus":2,"tel":"18546660142","expireTime":1720878173556,"isChoose":1,"areaCode":"86_CN","uniqueCode":"61faa60f69e305ff3f1d7da3cb8a78cd","imAppId":1400331755,"isRealName":1,"isAdmin":0,"userLevel":3,"memberExpireTime":0,"idtoken":"5947bc265aa9ce26666aff91b8f33e5a"}}'
# 自己15539502921
strs = '{"type":"object","data":{"st_flpv":"70qikoz9l1wawnbulxw77jbkehd9mktf","userId":9256095,"userType":1,"tuType":0,"userName":"蚍蜉渡海_","avatar":"https://s2.showstart.com/img/2024/0412/09/30/d5398f9b27374011b06dd4b77baa2b88_200_200_13964.0x0.png","loginTime":1718087319965,"sign":"cba36e01b753e18aeae8a723154a1e26","ticketWalletServiceStatus":2,"tel":"15539502921","expireTime":1720679319967,"isChoose":1,"areaCode":"86_CN","uniqueCode":"56cf13c5c37d4fa68c0e4f696e4ed592","imAppId":1400331755,"isRealName":2,"isAdmin":0,"userLevel":13,"memberExpireTime":0,"idtoken":"87a79e22fb8227886667f6cb525123ae","id":9256095,"name":"蚍蜉渡海_","isCollect":0,"creditLevel":0,"creditLevelExp":[20,131,420,1634,4257]}}'
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

time.sleep(2)
pay_btn = driver.find_elements(By.CLASS_NAME, "payBtn")[0]

# 定义确认方法
def start():
    while True:
      pay_btn.click()
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
        if minutes == '0' and seconds == '0':
            start()
            break
        time.sleep(0.001)  # 每0.001秒获取一次
finally:
    current_time = driver.execute_script(get_time_script)


