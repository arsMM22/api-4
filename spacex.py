import requests
from dowloand_image import download_image


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(url)
    for image_number, image in enumerate(
            response.json()['links']['flickr']['original']):
        download_image(image, f'images/spacex{image_number}.jpg')


def main():
    fetch_spacex_last_launch()


if __name__ == "__main__":
    main()
