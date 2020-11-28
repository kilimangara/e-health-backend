"""Модуль работы с sms."""
from urllib.parse import urlencode
from app.core.config import settings

import requests


def send_sms(sms_code: str, phone_number: str):
    # зависимость от конфига
    # сделать отправку смс в зависимости от окружения
    if settings.SMS_SENDER_ENABLED:
        params_dict = {
            "login": settings.SMS_SENDER_LOGIN,
            "psw": settings.SMS_SENDER_PASSWORD,
            "phones": phone_number,
            "mes": sms_code,
            "charset": "utf-8",
            "bin": "0",
            "sender": "E-Health",
            "fmt": 3,  # ответ в формате json
        }
        params_dict = urlencode(params_dict)
        url_get = "https://smsc.ru/sys/send.php?" + params_dict
        requests.get(url_get)
    # надо добавить логгер, и проверку на ошибки, может быть навернуть ретраи (логгер лежит в fastapi.logger)
