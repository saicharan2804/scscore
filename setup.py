from setuptools import setup, find_packages

setup(
    name='scscore',
    version='1.0.0',
    author='Connor Coley',
    author_email='YourEmail@example.com',
    description='A simple implementation of the SCScoring model',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/saicharan2804/scscore',
    package_data={
        'scscore': ['scscore/models/full_reaxys_model_1024bool/*', 'scscore/models/full_reaxys_model_2048uint/*'],
    },
    install_requires=[
        'numpy',  # Add other dependencies as required
        'rdkit',
    ],
)
