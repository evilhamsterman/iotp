# iotp
A small app for generating TOTP (Google Authenicator/RFC 6238 compatible) codes.

## Installation
`pip install .`

## Usage

### Add or modify a service
`iotp set <Service name> <Base32 Key>`

For example

`iotp Slack SQUE5WUI3XJQ4T7E`

### Retrieve a TOTP

For a all registered services

`iotp get`

For a specific service

`iotp get Slack`

### Remove a service

`iotp rm Slack`
