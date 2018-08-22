import requests
http_proxy  = "http://109.125.91.7:8080"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy   = "ftp://10.10.1.10:3128"





class teleBot:
    def __init__(self, token):
        self.proxie = "https://142.93.202.233:8080"
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params, proxies = {'https': self.proxie})
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params, proxies = {'https': self.proxie})
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update