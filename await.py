from selenium import webdriver
from selenium.webdriver.common.by import By
pip install requests
import time

# 设置Chrome浏览器的选项
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # 如果不需要浏览器界面，可启用无头模式
# options.add_argument('--disable-gpu')  # 适用于无头模式

# 初始化webdriver
driver = webdriver.Chrome(options=options)

# 打开指定的URL
url = 'https://wap.showstart.com/pages/order/activity/confirm/confirm?sequence=224243&ticketId=eed9589e63982d86e15b01678865520f&ticketNum=1'
driver.get(url)
time.sleep(2)

# 注入token
key = 'userInfo'
strs = '{"type":"object","data":{"st_flpv":"70qikoz9l1wawnbulxw77jbkehd9mktf","userId":9256095,"userType":1,"tuType":0,"userName":"蚍蜉渡海_","avatar":"https://s2.showstart.com/img/2024/0412/09/30/d5398f9b27374011b06dd4b77baa2b88_200_200_13964.0x0.png","loginTime":1718087319965,"sign":"cba36e01b753e18aeae8a723154a1e26","ticketWalletServiceStatus":2,"tel":"15539502921","expireTime":1720679319967,"isChoose":1,"areaCode":"86_CN","uniqueCode":"56cf13c5c37d4fa68c0e4f696e4ed592","imAppId":1400331755,"isRealName":2,"isAdmin":0,"userLevel":13,"memberExpireTime":0,"idtoken":"87a79e22fb8227886667f6cb525123ae","id":9256095,"name":"蚍蜉渡海_","isCollect":0,"creditLevel":0,"creditLevelExp":[20,131,420,1634,4257]}}'
driver.execute_script(f"window.localStorage.setItem('{key}', '{strs}');")
driver.get(url)

# 打印userInfo 确认成功
script = "return window.localStorage.getItem('userInfo');"
value = driver.execute_script(script)
print(value)


# 获取所有DOM元素
time.sleep(10)
def search():
    try:
        pay_btn = driver.find_elements(By.CLASS_NAME, "payBtn")
        print(pay_btn[0].text)
        if pay_btn[0].text == '已售罄':
            driver.refresh()
            time.sleep(3)
            search()
        else:
            # 打开观演人
            driver.find_elements(By.CLASS_NAME, "rr")[0].click()
            time.sleep(1)
            # 选择观演人
            driver.find_elements(By.CLASS_NAME, "uni-checkbox-input")[0].click()
            time.sleep(1)
            # 点击确定按钮
            confirm_button = driver.find_element(By.XPATH, '//uni-view[contains(text(), "确定")]')
            confirm_button.click()
            print('选择观演人')
            time.sleep(3)
            pay_btn.click()
    except Exception as e:
        search()
search()


