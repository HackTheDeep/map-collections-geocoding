from distutils.core import setup

setup(
    # Application name:
    name="collection_geo_locate",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Hack The Deep",
    author_email="name@addr.ess",

    # Packages
    packages=["see requirements.txt"],

    # Include additional files into the package
    include_package_data=True,

    #
    # license="LICENSE.txt",
    description="Get latitude and longetude from text based address data",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "bingmaps",
        "certifi",
        "chardet",
        "click",
        "decorator",
        "future",
        "geocoder",
        "googlemaps",
        "idna",
        "marshmallow",
        "ratelim",
        "requests",
        "six",
        "urllib3",
        "python-dateutil",
        "pyodbc",
        "xmltodict"
    ],
)