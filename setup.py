from setuptools import setup, find_packages

setup(
    name="crypto-com-ai-agent-client",
    version="1.0.4",
    description="Python client for Crypto.com AI Agent Service",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Ricardo Arcifa",
    author_email="rarcifa@gmail.com",
    url="https://github.com/crypto-com/cdc-ai-agent-client-py",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
