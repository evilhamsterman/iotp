from setuptools import setup

setup(
    name='iotp',
    author='Dan Mills',
    version='1.0.1',
    license='Apache 2.0',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
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
