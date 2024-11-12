import asyncio
import logging
import sys

from os import getenv
from dotenv import load_dotenv

from aiogram import Bot

from vk.methods import get_credentials, get_user_credentials

from main import main

load_dotenv()

logging.basicConfig(filename="./sferum_in.log", encoding="utf-8", level=logging.INFO, datefmt='%m/%d/%Y %I:%M:%S %p')


#	Заполнить тут
#########################################################################


vk_chat_ids = "##" # вставить свой id чата

cookie = "##" ## вставить свою куку remixdsid

#########################################################################
#	Заполнить тут


user = get_user_credentials(cookie)
access_token = user.access_token
creds = get_credentials(access_token)

loop = asyncio.get_event_loop()

try:   
    
    task2 = loop.create_task( main(
    	creds.server, 
    	creds.key, 
    	creds.ts,     	
    	vk_chat_ids, access_token, cookie, creds.pts))


    logging.info("Loop starting")
    loop.run_until_complete(task2) ## программа завершится когда закончит выполняться цикл в функции main

except KeyboardInterrupt:
    pass
except Exception as e:
    logging.exception(e)
finally:
    sys.exit(1)
    logging.info("Closing loop...")
    loop.close()
    logging.info("Loop closed")