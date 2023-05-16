
# -*- coding=utf-8 -*-
# Name: teddy oweh
# Email: teddy@teddyoweh.com
# Message: Feel Free To Contact Me on Enquires or Question, il Reply :)mport pathlib

from setuptools import setup, find_packages
import pathlib
 
HERE = pathlib.Path(__file__).parent

 
README = (HERE / "README.md").read_text()
 
setup(
    name="slicpy",
    version="0.0.3",
    description="Swift Low-latency Intercommunication)",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/teddyoweh/SLIC",
    author="Teddy Oweh",
    author_email="teddyoweh@gmail.com",
    packages=find_packages(),
    
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
  
    include_package_data=True,
    install_requires=['cryptography','requests','beardb'],
    entry_points={
        "console_scripts": [
            "SLIC=reader.__main__:main",
        ]
    },
)