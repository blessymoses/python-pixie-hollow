from setuptools import setup, find_packages

setup(
    name="bankpack",
    version="0.1",
    packages=find_packages(exclude=["tests*"]),
    license="none",
    description="Sample python package with pytest",
    long_description=open("README.md").read(),
    install_requires=[],
    url="REPOSITORY_URL",
    author="Blessy Moses",
    author_email="blessymoses17@gmail.com",
)
# https://blog.methodsconsultants.com/posts/pytesting-your-python-package/
