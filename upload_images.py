from time import sleep
import telegram
from os import listdir
import random
import os
from dotenv import load_dotenv


def main():
    sleep - 14400
    load_dotenv()
    tg_chat_id = os.environ['TG_CHAT_ID']
    tg_token = os.environ['TELEGRAM_TOKEN']
    bot = telegram.Bot(token=tg_token)
    while True:
        files = listdir("images")
        random.shuffle(files)
        for file in files:
            path = os.path.join("images", file)
            with open(path, "rb") as f:
                bot.send_document(chat_id=tg_chat_id, document=f)
            sleep(sleep)


if __name__ == "__main__":
    main()
