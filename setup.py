from setuptools import find_packages, setup

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='cyclus_gateway',
    version='0.1.0',
    license='BSD',
    maintainer='Yarden Livnat',
    description='A gateway for remove cyclus services',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'cyclus_gateway',
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
