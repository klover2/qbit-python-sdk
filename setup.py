import os

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

requires = [
    "requests>=2.28.1",
]

setuptools.setup(
    name="qbit_py_sdk",
    version="1.0.0",
    keywords=["qbit", "全球账户", "量子卡"],
    author="qbit team",
    author_email="w.klover@foxmail.com",
    description="qbit bass api 接口支持",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/klover2/qbit-python-sdk",
    packages=setuptools.find_packages(exclude=('tests', '.pypirc')),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=requires,
)
