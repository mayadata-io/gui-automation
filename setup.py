from setuptools import setup


VERSION = '1.0'

install_requires = [
    'pytest>=5.3.5',
    'pytest-rerunfailures>=4.1',
    'allure-pytest>=2.8.10',
    'allure-python-commons>=2.8.10'
]


def main():
    setup(
        name='MayaData-pytest',
        version=VERSION,
        description='MayaData Pytest testing framework',
        author='nrusinko',
        packages=['src'],
        url='https://account.mayadata.io',
        install_requires=install_requires
    )


if __name__ == '__main__':
    main()