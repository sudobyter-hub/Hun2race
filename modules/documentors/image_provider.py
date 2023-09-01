import os
from urllib.parse import urlparse

import requests


class ImageProvider:
    def __init__(self):
        pass

    def get_images_from_urls(self, urls):
        """ Downloads all images from a list of URLs """
        paths = []
        for url in urls:
            paths.append(self.download_image(url))
        return paths

    def download_image(self, url, save_path="downloaded_images"):
        """ Downloads an image from a URL and saves it to a specified path """
        if not self.validate_image_url(url):
            raise ValueError(f"URL {url} does not seem to point to a valid image.")

        response = requests.get(url, stream=True)
        response.raise_for_status()

        save_path = os.path.join(os.getcwd(), save_path, os.path.basename(urlparse(url).path))

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        return save_path

    def validate_image_url(self, url):
        """ Validates if the URL points to an image """
        parsed = urlparse(url)
        for ext in ['.jpg', '.jpeg', '.png', '.gif']:
            if parsed.path.endswith(ext):
                return True
        return False