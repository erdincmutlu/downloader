import os
import urllib.request
DEFAULT_DOWNLOADED_FOLDER = 'downloaded'
DEFAULT_RANGE = 20
DEFAULT_EXTENSION = 'jpg'


def download_with_numbered_names(web_link, save_path, r, extension):
    for n in range(r):
        try:
            file_name = f"{n}.{extension}"
            url = f"{web_link.rstrip('/')}/{file_name}"

            save_location = os.path.join(save_path, file_name)
            urllib.request.urlretrieve(url, save_location)
            print(f"Downloaded {file_name}")
        except Exception as e:
            print("url:{}\nexception: {}".format(url, e))


web_link = input("Web link: ")
save_path = input("Save path ({}): ".format(
    DEFAULT_DOWNLOADED_FOLDER)) or DEFAULT_DOWNLOADED_FOLDER
r = int(input("Range ({}): ".format(DEFAULT_RANGE)) or DEFAULT_RANGE)
extension = input("Extension ({}): ".format(
    DEFAULT_EXTENSION)) or DEFAULT_EXTENSION

download_with_numbered_names(
    web_link, save_path, r, extension)
