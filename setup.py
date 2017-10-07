from setuptools import setup
from i2paccess import __version__

url = "https://github.com/l-n-s/django-i2paccess/tarball/{0}".format(__version__)

with open("README.md") as readme:
    long_description = readme.read()

setup(
    name="django-i2paccess",
    version=__version__,
    author="Darknet Villain",
    author_email="supervillain@riseup.net",
    description=("Access control for I2P HTTP server tunnel in Django"),
    install_requires=[],
    license="MIT",
    keywords="django i2p",
    url=url,
    packages=["i2paccess",],
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        "Topic :: Utilities",
    ],
)
