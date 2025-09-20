import requests
import random
class Check(object):
    def __init__(self,username,proxy=None):
        self.proxy = {
            "http": "http://com100654271-zone-custom:2179803216@geo.iprocket.io:2224",
            "https": "http://com100654271-zone-custom:2179803216@geo.iprocket.io:2224"  
        }
        self.username = username
    def checking(self):
        android_versions = ["10", "11", "12", "13"]
        devices = ["SM-G960F", "SM-G930F", "SM-G998B", "SM-G991B", "SM-A515F", "SM-N975F", "SM-G780G", "SM-A525F", "SM-G998B", "SM-N9810"]
        chrome_versions = ["131.0.0.0", "130.0.0.0", "129.0.0.0", "128.0.0.0", "127.0.0.0"]
        build_versions = ["PPR1.180610.011", "RQ3A.210805.001", "SP1A.210812.016", "AOSP.210812.016", "QP1A.190711.020"]
        build_version = random.choice(build_versions)
        android_version = random.choice(android_versions)
        device = random.choice(devices)
        chrome_version = random.choice(chrome_versions)
        user_agent = f"Mozilla/5.0 (Linux; Android {android_version}; {device} Build/{build_version}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36"
        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'referer': 'https://www.instagram.com/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': user_agent,
            'viewport-width': '521',
            'x-asbd-id': '198387',
            'x-csrftoken': 'swHjV5IsFciWXXb90ey4sQ69N9RMjO8S',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR2Nc8ncW4a-SseKs1h3LLgACXFvdcRKTAAE6YA1rx97kl87',
            'x-instagram-ajax': '1006681141',
            'x-requested-with': 'XMLHttpRequest',
        }
        params = {'count': '12',}
        try:
            response = requests.post(f'https://www.instagram.com/api/v1/feed/user/{self.username}/username/',params=params,headers=headers).json()
            print(response)
        except Exception as e:
            print(e)
            return None
        if response["status"] == "fail":
            return None
        try:
            response["user"]["username"]
            return True
        except:
            return False

# while True:
#     check = Check(username="lmccoy_877364").checking()
#     if check == None or check == False: break
#     break

#   {'message': 'Vui lòng chờ vài phút trước khi thử lại.', 'require_login': True, 'igweb_rollout': True, 'status': 'fail'}
