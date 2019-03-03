import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

    name='las-converter',

    version='0.1',

    scripts=['converter'],

    author="Jose Sitanggang, Asido Sigalingging",

    author_email="jose.stnggng@gmail.com,asido.saputra@gmail.com",

    description="Converter LAS file to python dictionary and json file",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="https://github.com/josestnggng/Las-converter",

    packages=setuptools.find_packages(),

    classifiers=[

        "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

    ],

)
