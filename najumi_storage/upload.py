import requests


def upload(
    self,
    file_path,
    path="/",
):
    with open(
        file_path,
        "rb",
    ) as file:

        response = requests.post(
            f"{self.base_url}/api/storage/upload",
            headers=self.headers(),
            data={
                "path": path,
            },
            files={
                "file": file,
            },
        )

    response.raise_for_status()

    return response.json()
