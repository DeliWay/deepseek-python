from setuptools import setup, find_packages

setup(
    name="deepseek",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "aiohttp>=3.9.0",
        "markdown>=3.3.0",
        "autopep8>=2.0.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="Python клиент для DeepSeek Chat API с кешированием и форматированием",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/deepseek-python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
)