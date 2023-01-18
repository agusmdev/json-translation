from setuptools import setup, find_packages

setup(
    name='json-translation',
    version='1.0.0',
    author='Agustin Marchi',
    url='https://github.com/agusmdev',
    packages=find_packages(),
    license='LICENSE',
    description='json-translation',
    long_description=open('README.md').read(),
    install_requires= [ 
        "boto3>=1.26.48",
        "botocore>=1.29.48"
     ] # complete your module dependencies
)
