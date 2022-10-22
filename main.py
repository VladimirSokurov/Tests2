import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_folder(self, folder):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/"
        headers = self.get_headers()
        params = {"path": folder}
        response = requests.put(upload_url, headers=headers, params=params)
        response.raise_for_status()
        return response.status_code


if __name__ == '__main__':
    folder = "new_folder123231321"
    token = "AQAAAAAE1VytAADLW4tlzb4WCkFJhNKom7YrJM0"

    uploader = YaUploader(token)
    result = uploader.create_folder(folder)
