from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

# 设置Chrome浏览器的选项
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 如果不需要浏览器界面，可启用无头模式
# options.add_argument('--disable-gpu')  # 适用于无头模式

# 初始化webdriver
driver = webdriver.Chrome()

# 打开指定的URL
url = 'https://wap.showstart.com/pages/order/activity/confirm/confirm?sequence=224240&ticketId=d20e7866d079ed30353d1ede92f531e1&ticketNum=1'
driver.get(url)
time.sleep(3)

user_info = {
        "type": "object",
        "data": {
            "st_flpv": "70qikoz9l1wawnbulxw77jbkehd9mktf",
            "userId": 9256095,
            "userType": 1,
            "tuType": 0,
            "userName": "蚍蜉渡海_",
            "avatar": "https://s2.showstart.com/img/2024/0412/09/30/d5398f9b27374011b06dd4b77baa2b88_200_200_13964.0x0.png",
            "loginTime": 1717059232891,
            "sign": "bbdaa16973fe476fd60e02c9f3547151",
            "ticketWalletServiceStatus": 2,
            "tel": "15539502921",
            "expireTime": 1719651232893,
            "isChoose": 1,
            "areaCode": "86_CN",
            "uniqueCode": "56cf13c5c37d4fa68c0e4f696e4ed592",
            "imAppId": 1400331755,
            "isRealName": 2,
            "isAdmin": 0,
            "userLevel": 13,
            "memberExpireTime": 0,
            "idtoken": "91fb23d1611a8ccb665846d41e3c1b87",
            "id": 9256095,
            "name": "蚍蜉渡海_",
            "isCollect": 0,
            "creditLevel": 0,
            "creditLevelExp": [20, 131, 420, 1634, 4257]
        }
    }
    # 将 userInfo 转换为 JSON 字符串
user_info_json = json.dumps(user_info)
key = 'userInfo'
strs = '{"type":"object","data":{"st_flpv":"70qikoz9l1wawnbulxw77jbkehd9mktf","userId":9256095,"userType":1,"tuType":0,"userName":"蚍蜉渡海_","avatar":"https://s2.showstart.com/img/2024/0412/09/30/d5398f9b27374011b06dd4b77baa2b88_200_200_13964.0x0.png","loginTime":1717059232891,"sign":"bbdaa16973fe476fd60e02c9f3547151","ticketWalletServiceStatus":2,"tel":"15539502921","expireTime":1719651232893,"isChoose":1,"areaCode":"86_CN","uniqueCode":"56cf13c5c37d4fa68c0e4f696e4ed592","imAppId":1400331755,"isRealName":2,"isAdmin":0,"userLevel":13,"memberExpireTime":0,"idtoken":"91fb23d1611a8ccb665846d41e3c1b87","id":9256095,"name":"蚍蜉渡海_","isCollect":0,"creditLevel":0,"creditLevelExp":[20,131,420,1634,4257]}}'
# print(user_info_json)
driver.execute_script(f"window.localStorage.setItem('{key}', '{strs}');")

driver.get(url)

script = "return window.localStorage.getItem('userInfo');"
value = driver.execute_script(script)
print("localStorage value for 'userInfo':", value)

# 获取所有DOM元素
elements = driver.find_elements(By.XPATH, "//*")

# 输出所有DOM元素的标签名
# for element in elements:
#     print(element.tag_name)

# 关闭webdriver
# driver.quit()
#好问题
