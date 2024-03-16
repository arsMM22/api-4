import requests
from dowloand_image import download_image


def fetch_spacex_last_launch(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    for image_number, image in enumerate(
            response.json()['links']['flickr']['original']):
        download_image(image, f'images/spacex{image_number}.jpg')


def main():
    parser = argparse.ArgumentParser(
        description='Эта программа позволит вам загрузить фотографии с запуска SpaceX.'
    )
    parser.add_argument(
        '--id',
        dest='launch_id',
        default="5eb87d47ffd86e000604b38a",
        help='Укажите ID запуска SpaceX, с которого можно загрузить фотографии.'
    )
    args = parser.parse_args()
    fetch_spacex_last_launch(args.launch_id)


if __name__ == "__main__":
    main()
