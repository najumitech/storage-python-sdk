from .stats import stats
from .files import files
from .upload import upload
from .download import download
from .delete import delete

class Storage:
    def __init__(
        self,
        bucket_id,
        access_key,
        secret_key,
        base_url="https://storage-api.najumitech.com",
    ):
        self.base_url = base_url
        self.bucket_id = bucket_id
        self.access_key = access_key
        self.secret_key = secret_key

    def headers(self):
        return {
            "x-bucket-id": self.bucket_id,
            "x-access-key": self.access_key,
            "x-secret-key": self.secret_key,
        }

Storage.stats = stats
Storage.files = files
Storage.upload = upload
Storage.download = download
Storage.delete = delete
