# iotp
A small app for generating TOTP (Google Authenicator/RFC 6238 compatible) codes.

## Installation
`pip install .`

## Usage

### Add or modify a service
`iotp set <Service name> <Base32 Key>`

For example:

`iotp Slack SQUE5WUI3XJQ4T7E`

### Retrieve a TOTP

For a all registered services

`iotp get`

For a specific service

`iotp get [-c] <service>`

Using `-c` will copy the code to the clipboard. This requires installing the `xclip` app on Linux/\*BSD, Windows and Mac have not extra requirements.

For example:

`iotp get -c Slack`

then Ctrl-v into your authentication dialog


### Remove a service

`iotp rm <service>`

For example

`iotp rm Slack`
