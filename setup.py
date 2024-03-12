from setuptools import setup, find_packages

setup(
    name = "cpp",
    version = "1.1",
    packages = find_packages(),
    author = "Sahil Rajwar",
    description = "A Python lib for compiling & running C++ code",
    long_description = open("README.md","r").read(),
    long_description_content_type = 'text/markdown',
    url = "https://github.com/Sahil-Rajwar-2004/cpp.py",
    license = open("LICENSE.txt","r").read(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
