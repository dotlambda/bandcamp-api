from setuptools import *

setup(
    name="bandcamp_api",
    version="0.1.01",
    description="Obtains information from bandcamp.com",
    author="RustyRin",
    packages=['bandcamp_api'],
    url="https://github.com/RustyRin/bandcamp-api/",
    install_requires=["setuptools", "bs4", "demjson3"],
    zip_safe=False
    )