import requests


def delete(
    self,
    shield,
):
    response = requests.post(
        f"{self.base_url}/api/storage/delete",
        headers=self.headers(),
        data={
            "shield": shield,
        },
    )

    response.raise_for_status()

    return response.json()
