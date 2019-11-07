import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='deezersdk',
    version='0.15',
    packages=setuptools.find_packages(),
    author="Gomes Alexis",
    author_email="alexis.gomes19@gmail.com",
    description="A python SDK for the Deezer API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlexisGomes/deezersdk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
