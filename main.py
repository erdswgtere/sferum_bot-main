import logging
import requests
import random
import string

from asyncio import sleep

from vk.methods import get_credentials, get_user_credentials, get_message , send_message
from vk.types import Message, EventMessage

async def main(server, key, ts, vk_chat_ids, access_token, cookie, pts):
    a: int = 0
    data = {
        "act": "a_check",
        "key": key,
        "ts": ts,
        "wait": a
    }
    for i in range(1, 6) : # при необходимости посылать сообщения бесконечно заменить на бесконечный цикл н.п while(true)
        await sleep(a)
        res = ''.join(random.choices(string.ascii_letters,
                                     k=random.randint(10, 20)))  # регулировка длины отправляемой строки
        print(str(res))
        print(a)
        try:
           a: int = random.randint(10, 15) # регулировка интервала отправкии сообщений(через сколько будет отправлено следующее сообщение)
           print("Send message")

           send_message(access_token , vk_chat_ids , res);

        except Exception as e:
            logging.exception(e)

