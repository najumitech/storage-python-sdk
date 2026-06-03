from setuptools import (
    setup,
    find_packages,
)

with open(
    "README.md",
    "r",
    encoding="utf-8",
) as fh:
    long_description = fh.read()

setup(
    name="najumi-storage",
    version="1.0.0",
    description="Official Python SDK for Najumi Storage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Najumi Tech",
    author_email="info@najumitech.com",
    maintainer="Najumi Tech",
    maintainer_email="info@najumitech.com",
    url="https://github.com/najumitech/storage-python-sdk",
    project_urls={
        "Homepage":
            "https://najumitech.com",
        "Documentation":
            "https://github.com/najumitech/storage-python-sdk",
        "Source":
            "https://github.com/najumitech/storage-python-sdk",
        "Issues":
            "https://github.com/najumitech/storage-python-sdk/issues",
        "Changelog":
            "https://github.com/najumitech/storage-python-sdk/releases",
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests>=2.31.0",
    ],
    keywords=[
        "najumi",
        "storage",
        "cloud",
        "cloud-storage",
        "object-storage",
        "sdk",
        "python",
        "api",
        "upload",
        "download",
        "file-storage",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    license="MIT",
    zip_safe=False,
)
