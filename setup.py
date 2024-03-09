from setuptools import setup, find_packages

setup(
    name = "cpp",
    version = "1.0",
    packages = find_packages(),
    author = "Sahil Rajwar",
    description = "A Python class for compiling & running C++ code",
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    url = "https://github.com/Sahil-Rajwar-2004/cpp.py",
    license = "MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

