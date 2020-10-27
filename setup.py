from setuptools import setup, find_packages

setup(
    name='gcg',
    version='1',
    url='http://www.github.com/cbaxter1988',
    description='Genesis Configuration Generator',
    author='Courtney S Baxter Jr',
    author_email='cbaxtertech@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'gcg-cli=gcg.__main__:main'
        ]
    }
)
