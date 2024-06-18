from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
response = requests.post('http://116.62.122.121:4397/postMsg',data={'text':'aaaa'},headers={})
# 设置Chrome浏览器的选项
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # 如果不需要浏览器界面，可启用无头模式
# options.add_argument('--disable-gpu')  # 适用于无头模式

# 初始化webdriver
driver = webdriver.Chrome(options=options)

# 打开指定的URL 南昌
url = 'https://wap.showstart.com/pages/order/activity/confirm/confirm?sequence=224243&ticketId=eed9589e63982d86e15b01678865520f&ticketNum=1'
driver.get(url)
time.sleep(2)

# 注入token
key = 'userInfo'
# zyp
strs = '{"type":"object","data":{"st_flpv":"4hzgsxjbn8un7k00mwm609ykc76hu6nq","userId":9261885,"userType":1,"tuType":0,"userName":"紫玉天青","avatar":"https://s2.showstart.com/img/2024/0412/09/30/d5398f9b27374011b06dd4b77baa2b88_200_200_13964.0x0.png","loginTime":1718677895276,"sign":"66a2e864b8cea6dc8d987d58152866c7","ticketWalletServiceStatus":2,"tel":"17854251778","expireTime":1721269895278,"isChoose":1,"areaCode":"86_CN","uniqueCode":"605cc6db07f3a8a75f5d3f74446c7538","imAppId":1400331755,"isRealName":2,"isAdmin":0,"userLevel":13,"memberExpireTime":0,"idtoken":"e024d61d34d114186670f9bbde5e5cac","id":9261885,"name":"紫玉天青","isCollect":0,"creditLevel":0,"creditLevelExp":[20,131,420,1634,4257]}}'
driver.execute_script(f"window.localStorage.setItem('{key}', '{strs}');")
driver.get(url)

# 打印userInfo 确认成功
script = "return window.localStorage.getItem('userInfo');"
value = driver.execute_script(script)
print(value)


# 获取所有DOM元素
time.sleep(5)
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
            time.sleep(2)
            print('可以下单')
            # 点击下单
            pay_btn[0].click()
            payload = {'text':'有余票！请立即支付！账号紫玉天青'}
            response = requests.post('http://116.62.122.121:4397/postMsg',data=payload,headers={})
            # 点击支付
            time.sleep(2)
            driver.find_elements(By.CLASS_NAME, "alipay")[0].click()
            time.sleep(10)
    except Exception as e:
        # search()
        print('结束')
search()


