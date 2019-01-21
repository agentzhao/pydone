import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydone",
    version="1.5.4",
    author="AI lmao",
    author_email="tan.hongzhao@dhs.sg",
    description="A small python library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Agentzhao/pydone",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
