from setuptools import find_packages, setup

setup(
    name='cyclus_gateway',
    version='0.2.0',
    license='BSD',
    maintainer='Yarden Livnat',
    description='A gateway for remove cyclus services',
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
