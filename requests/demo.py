import requests

# response=requests.get("https://www.baidu.com")
# print(response.text)


# pay_load={"loginId":"40","password":"123456","orgId":11}
# response=requests.post("http://acv3.learn.it101.live/api/auth/login",pay_load)
# print(response.json())

# header={"ac-token":"gYvU_6C43-fb6jypnVEqqf5UQbWudETy"}
# response=requests.get("http://acv3.learn.it101.live/api/courses/v3/trends",headers=header)
# date= response.json()
# assert date['ok']==True

# 打印HTTP响应消息函数
def printResponse(response):
    print('\n\n--------HTTP response *begin--------------')
    print(response.status_code)  # 获取状态码
    # 获取内容
    for k, v in response.headers.items():
        print(f'{k}:{v}')
    print(" ")
    print(response.content.decode('utf8'))  # 编码
    print('\n\n--------HTTP response *end----------------')


# 使用session
session = requests.session()
pay_load = {"loginId": "40", "password": "123456", "orgId": 11}
response = session.post("http://acv3.learn.it101.live/api/auth/login", pay_load)
printResponse(response)

response = session.get("http://acv3.learn.it101.live/api/courses/v3/trends")
printResponse(response)
