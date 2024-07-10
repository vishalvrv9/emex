from setuptools import setup, find_packages

setup(
    name='emex',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'cmd2',
        "mlx", 
        "mlx_lm"
    ],
    entry_points={
        'console_scripts': [
            'emex=emex.main:main',
        ],
    },
)
