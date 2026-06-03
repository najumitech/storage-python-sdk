import requests


def download(
    self,
    shield,
    output_path,
):
    response = requests.get(
        f"{self.base_url}/api/storage/download/{shield}",
        headers=self.headers(),
        stream=True,
    )

    response.raise_for_status()

    with open(
        output_path,
        "wb",
    ) as file:
        for chunk in response.iter_content(
            chunk_size=8192
        ):
            if chunk:
                file.write(
                    chunk
                )

    return output_path
