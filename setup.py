from setuptools import find_packages
from setuptools import setup

setup(
    name="revChatGPT",
    version="2.1.5",
    license="GNU General Public License v2.0",
    author="Antonio Cheong",
    author_email="acheong@student.dalat.org",
    description="ChatGPT is a reverse engineering of OpenAI's ChatGPT API",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=["Unofficial", "V2", "Proxied"],
    url="https://github.com/acheong08/ChatGPT",
    install_requires=[
        "asyncio",
        "httpx",
        "OpenAIAuth==0.1.1",
        "tiktoken",
    ],
    extras_require={
        "unofficial": [
            "requests",
            "undetected_chromedriver",
            "selenium",
            "tls_client",
            "requests",
        ],
    },
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
)
