import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="decision",
    version="0.1.1",
    author="Brett McSweeney",
    author_email="brett_mcs@optusnet.com.au",
    description="A python project for make decisions using a fuzzy flow chart",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BrettMcS/decision",
    packages=setuptools.find_packages(exclude=['docs', 'tests*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)