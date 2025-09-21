import requests
import random
class Check(object):
    def __init__(self,username,proxy=None):
        self.proxy = {
            "http": "http://ZP20160_NFQPcx:M8NQSIg6__country-vn_session-t4wnlq8q_lifetime-m@amz5.zingproxy.com:11222",
            "https": "http://ZP20160_NFQPcx:M8NQSIg6__country-vn_session-t4wnlq8q_lifetime-m@amz5.zingproxy.com:11222"  
            #amz5.zingproxy.com:11222:ZP20160_NFQPcx:M8NQSIg6__country-vn_session-t4wnlq8q_lifetime-m
        }
        self.username = username
    def checking(self):
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'cookie': 'ig_did=2F6B1652-1252-4519-B7C1-FCCEBE936429; csrftoken=iARQv8L1zQoK3fGieZlkj7; datr=7ArQaHL5TWqusnvocJGXGd10; mid=aNAK7AAEAAF_sxQf21uzBiO7RwS8; wd=499x857',
            'dpr': '1.5',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6834.196", "Google Chrome";v="132.0.6834.196"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
            'viewport-width': '434',
        }
        try:
            response = requests.get(f'https://www.instagram.com/{self.username}/', proxies=self.proxy)
            # print(response.text)
        except:
            return None
        if '"success_status":"success"' in response.text:
            print(response.url)
            try:
                if response.text.split('"query":{"username":"')[1].split('"')[0] == self.username:
                    return True
                return None
            except Exception as e:
                print(str(e))
                return False
        return None

# while True:
#     check = Check(username="ksdfn").checking()
#     print(check)
    # if check == None or check == False: break
    # break

#   {'message': 'Vui lòng chờ vài phút trước khi thử lại.', 'require_login': True, 'igweb_rollout': True, 'status': 'fail'}
