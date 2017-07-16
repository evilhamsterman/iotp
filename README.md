# iotp
A small app for generating TOTP (Google Authenicator/RFC 6238 compatible) codes.

## Installation
`pip install .`

## Usage

### Add or modify a service
`iotp set <Service name> <Base32 Key>`

Keys with spaces must be entered in quotes

For example:

`iotp set Slack "SQUE 5WUI 3XJQ 4T7E"`

or

`iotp set Slack "SQUE5WUI3XJQ4T7E"`


### Retrieve a TOTP

For a all registered services

`iotp get [-cCr]`

For a specific service

`iotp get [-cCr] <service>`

By default a countdown bar will display the remaining seconds the TOTP is valid.
* `-c` will copy the code to the clipboard. This requires installing the `xclip` app on Linux/\*BSD, Windows and Mac have no extra requirements.
* `-C` will prevent the countdown from displaying.
* `-r` will repeat the TOTP after the countdown is over for the number specified.

For example:

`iotp get -c Slack`

then Ctrl-v into your authentication dialog


### Remove a service

`iotp rm <service>`

For example

`iotp rm Slack`
