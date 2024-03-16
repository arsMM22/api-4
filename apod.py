import requests
from urllib.parse import unquote, urlparse
import os
from dowloand_image import download_image
from dotenv import load_dotenv


def get_extension_link(link):
    decoded_url = unquote(link)
    parsed_link = urlparse(decoded_url)
    path, fullname = os.path.split(parsed_link.path)
    file_name, extension = os.path.splitext(fullname)
    return extension, file_name


def fetch_apond_images():
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        "api_key": nasa_token,
        "count": 1
    }
    response = requests.get(url, params=params)
    for nasa_image in response.json():
        if nasa_image.get("media_type") == 'image':
            nasa_link_image = nasa_image.get('hdurl') or nasa_image.get('url')
        extension, file_name = get_extension_link(nasa_link_image)
        path = os.path.join('images', f'{file_name}{extension}')
        download_image(nasa_link_image, path)


def main():
    load_dotenv()
    fetch_apond_image()
    nasa_token = os.environ['NASA_TOKEN']


if __name__ == "__main__":
    main()
