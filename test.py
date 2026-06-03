from najumi_storage import Storage

storage = Storage(
    bucket_id="njs_bucket_75f9cb59f4093969",
    access_key="njs_acc_43222ce64a9cec410117113e",
    secret_key="njs_sec_ba2bb056226bae6d2d3b4aa684d51c7727144b1e6f80616d",
    base_url="https://storage-api.najumitech.com",
)

print("\n=== STATS TEST ===")
stats = storage.stats()
print(stats)

print("\n=== FILES TEST ===")
files = storage.files()
print(files)

print("\n=== UPLOAD TEST ===")
upload_result = storage.upload(
    "sdk-test.txt"
)
print(upload_result)

shield = upload_result.get("shield")

if shield:

    print("\n=== DOWNLOAD TEST ===")

    download_result = storage.download(
        shield,
        "sdk-downloaded.txt"
    )

    print(download_result)

    print("\n=== DELETE TEST ===")

    delete_result = storage.delete(
        shield
    )

    print(delete_result)

else:

    print(
        "\nUpload response did not return a shield."
    )

print("\n=== FINAL FILES TEST ===")
print(storage.files())

print("\n=== ALL TESTS COMPLETED ===")
