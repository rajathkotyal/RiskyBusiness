import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="riskybusiness",
    version="0.0.1",
    author="Rajath Kotyal",
    author_email="rajathkotyal@gmail.com",
    description="A Python Library containing various functions to analyse the risk of a business.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://rajathkotyal.github.io",
    packages=setuptools.find_packages(),
    install_requires=['pandas',
                    'numpy>=1.14.5',
                    'matplotlib>=2.2.0'] ,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
