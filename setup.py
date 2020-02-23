from setuptools import setup

setup(
    name='makehook',
    version='0.1.0',
    entry_points={
        'console_scripts': [
            'makehook = makehook.__main__:main'
        ]
    },
)
