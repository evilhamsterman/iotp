#!/usr/bin/env python

# Import system libraries
import base64
import json
import os
import time
from datetime import datetime

# Import PyPi libraries
from appdirs import AppDirs
import click
import pyotp
import pyperclip

# Set app information
appname = 'iotp'
appauthor = 'Dan Mills'
appversion = '1.0.1'

# Setup appdirs
dirs = AppDirs(appname, appauthor)
keyFile = os.path.join(dirs.user_data_dir, 'keys.json')


def setup_keys():
    """
    Check for data file and directory and create if is doesn't exist

    Returns a dictionary of saved keys
    """
    if not os.path.isdir(dirs.user_data_dir):
        os.makedirs(dirs.user_data_dir)

    try:
        with open(keyFile, 'r') as f:
            keys = json.load(f)
    except ValueError:
        keys = {}
    except IOError:
        open(keyFile, 'w').close()
        keys = {}

    return keys


def save_keys(keys):
    """Takes a dictionary of keys and then saves them to the keys file"""
    with open(keyFile, 'w') as f:
        json.dump(keys, f, indent=True)


def get_totp(key, keyTime):
    """
    Accepts a BASE32 encoded key and returns the TOTP if it is valid and None
    if it is invalid
    """
    try:
        totp = pyotp.TOTP(key)
        return totp.at(keyTime)
    except TypeError:
        return None


def display_remaining(keyTime):
    """
    Displays a progress bar with the time remaining till the next 30 second
    """
    r = range(30, 0, -1)

    # Seconds remaining in block
    if keyTime.second > 30:
        secRemain = 30 - (keyTime.second - 30)
    else:
        secRemain = 30 - keyTime.second

    with click.progressbar(r,
                           label='Seconds Remaining',
                           width=30,
                           show_percent=False,
                           show_eta=False,
                           item_show_func=str) as bar:
        for i in bar:
            # Only wait a second if the countdown is less than the Seconds
            # remaining
            if i <= secRemain:
                time.sleep(1)


@click.group()
@click.version_option(appversion)
def cli():
    """
    iotp is a Google Authenicator/RFC 6238 compatible application for
    generating Time based One Time Passwords
    """
    pass


@cli.command()
@click.argument('service', required=False)
@click.option('--copy', '-c', is_flag=True, help="Copy TOTP to the clipboard")
@click.option('--repeat', '-r', default=1, help="Repeat TOTP after countdown")
@click.option('--count/--no-count', ' /-C', default=True, help="Display seconds remaining")
def get(copy, repeat, count, service=None):
    """
    Gets TOTP codes for service specified. If no service is specified it
    prints codes for all services
    """
    keys = setup_keys()
    while repeat:
        if len(keys) == 0:
            click.echo('No keys. Use iotp set to add one')
            break
        keyTime = datetime.now()
        if not service:
            for service in keys:
                value = keys[service]
                totp = get_totp(value, keyTime)
                if totp:
                    click.echo('{}: {}'.format(service, totp))
                    if copy and len(keys) == 1:
                        pyperclip.copy(totp)
            if count:
                display_remaining(keyTime)

        elif service in keys:
            totp = get_totp(keys[service], keyTime)
            if totp:
                click.echo('{}: {}'.format(service, totp))
                if copy:
                    pyperclip.copy(totp)
            else:
                click.echo('Key is invalid, please reset key')
            if count:
                display_remaining(keyTime)
        else:
            click.echo('{} does not exist'.format(service))
            break
        time.sleep(0.5)
        repeat-=1


@cli.command(help="Sets the service key")
@click.argument('service')
@click.argument('key')
def set(service, key):
    """Accepts a service and a key and saves it out to the keyFile."""
    keys = setup_keys()
    try:
        base64.b32decode(key)
    except TypeError:
        click.echo('{} is not a valid key'.format(key))
    else:
        keys[service] = key
        save_keys(keys)


@cli.command(help="Removes the specified service")
@click.argument('service')
def rm(service):
    """Accepts a service and removes it from the list of services."""
    keys = setup_keys()
    if keys.pop(service, None):
        click.echo('Removed {}'.format(service))
        save_keys(keys)
    else:
        click.echo('{} does not exist'.format(service))


if __name__ == '__main__':
    cli()
