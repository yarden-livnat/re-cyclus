from setuptools import find_packages, setup

setup(
    name='recyclus_gateway',
    version='0.2.0',
    license='BSD',
    maintainer='Yarden Livnat',
    description='A gateway for remove cyclus services',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
