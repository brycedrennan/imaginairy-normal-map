import subprocess
from functools import lru_cache

from setuptools import find_packages, setup


@lru_cache()
def get_git_revision_hash() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("ascii").strip()


revision_hash = get_git_revision_hash()

with open("README.md", encoding="utf-8") as f:
    readme = f.read()
    readme = readme.replace(
        '<img src="',
        f'<img src="https://raw.githubusercontent.com/brycedrennan/imaginairy-normal-map/{revision_hash}/',
    )

setup(
    name="imaginairy-normal-map",
    version="0.0.3",
    description="Image-to-normal-map ",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Bryce Drennan",
    # author_email="b r y p y d o t io",
    packages=find_packages(
        include=["imaginairy_normal_map", "imaginairy_normal_map.*"]
    ),
    include_package_data=True,
    install_requires=[
        "torch >= 1.7",
        "torchvision",
        "timm",
        "huggingface_hub",
    ],
    python_requires=">=3.7",
)
