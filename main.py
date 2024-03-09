from time import sleep
import telegram
from os import listdir
import random
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    tg_token = os.environ['TELEGRAM_TOKEN']
    bot = telegram.Bot(token=tg_token)
    bot.send_document(chat_id="@spacebot1234",
                      document=open('images/spacex0.jpg', 'rb'))
    while True:
        files = listdir("images")
        random.shuffle(files)
        for file in files:
            path = os.path.join("images", file)
            with open(path, "rb") as f:
                bot.send_document(chat_id="@spacebot1234", document=f)
            sleep(14400)


if __name__ == "__main__":
    main()
