from setuptools import setup

setup(
    name='iotp',
    author='Dan Mills',
    version='0.0.2',
    description='A CLI app for TOTP',
    py_modules=['iotp'],
    install_requires=[
        'click',
        'pyotp',
        'appdirs',
        'pyperclip'
    ],
    entry_points={
        'console_scripts': [
            'iotp=iotp:cli'
        ]
    }
)
