import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="create-python-app",
    version="0.0.1",
    author="leafwind",
    author_email="leafwind.cs@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leafwind/create-python-app",
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
    install_requires=[
    ],
)
