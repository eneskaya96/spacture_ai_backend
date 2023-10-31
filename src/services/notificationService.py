import requests


class NotificationService:
    tokens = ["ExponentPushToken[ML2SsYPpQ6vh-srte1AlfB]" ]

    def send_push_notification(self, token, message, title):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'exp.host'
        }
        payload = {
            'to': token,
            'sound': 'default',
            'title': title,
            'body': message
        }
        response = requests.post('https://exp.host/--/api/v2/push/send', headers=headers, json=payload)
        return response.json()

    def addToken(self, token):
        if token in self.tokens:
            return 'Token already saved', 200

        self.tokens.append(token)
        return 'Token saved successfully', 201

    def send_notification(self):
        title = "SUSPICIOUS ALERT"
        message = "Suspicious behaviour detected"
        for token in self.tokens:
            print(token)
            self.send_push_notification(token=token, title=title, message=message)
