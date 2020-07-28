"""Модуль работы с sms."""
import requests
from urllib.parse import urlencode


def send_sms(sms_code: str, phone_number: str):
    params_dict = {
        "login": "kilimangara",
        "psw": "131196",
        "phones": phone_number,
        "mes": sms_code,
        "charset": "utf-8",
        "bin": "0",
        "sender": "E-Health",
        "fmt": 3 # ответ в формате json
    }
    params_dict = urlencode(params_dict)
    url_get = "https://smsc.ru/sys/send.php?" + params_dict
    requests.get(url_get)
    # надо добавить логгер, и проверку на ошибки, может быть навернуть ретраи (логгер лежит в fastapi.logger)
