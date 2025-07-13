from setuptools import setup, find_packages

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "A utility library with useful Python helpers."

setup(
    name='pyhelperag',
    version='0.1.3',
    packages=find_packages(),
    author='Your Name',
    author_email='you@example.com',
    description='A utility library with useful Python helpers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_library',
    classifiers=[
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'pandas>=1.0.0'
    ],
)