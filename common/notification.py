import requests

from config import conf


# color: blue, wathet, turquoise, green, yellow, orange, red, carmine, violet, purple, indigo, grey
# 常用: green, yellow, orange, red
def notify(header: str, msg: str, color: str):
    headers = {'Content-Type': 'application/json'}
    appid = conf().get("appid")
    data = {
        "msg_type": "interactive",
        "card": {
            "config": {
                "wide_screen_mode": True
            },
            "header": {
                "title": {
                    "tag": "plain_text",
                    "content": header
                },
                "template": color
            },
            "elements": [
                {
                    "text": {
                        "tag": "plain_text",
                        "content": f"appid: {appid}"
                    },
                    "tag": "div"
                },
                {
                    "text": {
                        "tag": "plain_text",
                        "content": f"msg: {msg}"
                    },
                    "tag": "div"
                }
            ]
        }
    }
    webhook = conf().get("webhook")
    if webhook:
        requests.post(webhook, json=data, headers=headers)
