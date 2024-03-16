import requests
import os
from datetime import datetime
from dowloand_image import download_image
from dotenv import load_dotenv


def epic_images():
    nasa_token = os.environ['NASA_TOKEN']
    url = 'https://api.nasa.gov/EPIC/api/natural/image'
    params = {
        "api_key": nasa_token,
        "count": 2
    }
    response = requests.get(url, params=params)
    for epic_images in response.json():
        epic_date = epic_images['date']
        epic_date = datetime.fromisoformat(epic_date).strftime("%Y/%m/%d")
        epic_name = epic_images['image']
        epic_url = f"https://api.nasa.gov/EPIC/archive/natural/{epic_date}/png/{epic_name}.png"
        epic_path = os.path.join('images', f'{epic_name}.png')
        download_image(epic_url, epic_path)


def main():
    load_dotenv()
    epic_image()


if __name__ == "__main__":
    main()
