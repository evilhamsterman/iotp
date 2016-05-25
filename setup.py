from setuptools import setup

setup(
    name='iotp',
    author='Dan Mills',
    version='0.0.1',
    description='A CLI app for TOTP',
    py_modules=['iotp'],
    install_requires=[
        'click',
        'pyotp'
    ],
    entry_points={
        'console_scripts': [
            'iotp=iotp:cli'
        ]
    }
)
