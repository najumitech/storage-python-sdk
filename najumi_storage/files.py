import requests


def files(self):
    response = requests.get(
        f"{self.base_url}/api/storage/files",
        headers=self.headers(),
    )

    response.raise_for_status()

    return response.json()
