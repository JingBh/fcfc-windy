import setuptools

with open("README.md", "rb") as fh:
    long_description = fh.read().decode()

setuptools.setup(
    name="fcfc-windy",
    version="0.2.0",
    author="JingBh",
    author_email="jingbohao@yeah.net",
    description="Windy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    repository_url="https://github.com/JingBh/fcfc-windy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "Natural Language :: Xiglish",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)
