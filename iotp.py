#!/usr/bin/env python

import os
import pyotp
import json
import base64
# import click
from appdirs import AppDirs

# Set app information
appname = 'iotp'
appauthor = 'Dan Mills'

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
        print("File exists but is empty")
        keys = {}
    except IOError:
        print("File does not exist")
        open(keyFile, 'w').close()
        keys = {}

    return keys


def save_keys(keys):
    """Takes a dictionary of keys and then saves them to the keys file"""
    with open(keyFile, 'w') as f:
        json.dump(keys, f, indent=True)


def get_totp(key):
    """
    Accepts a BASE32 encoded key and returns the TOTP if it is valid and None
    if it is invalid
    """
    try:
        totp = pyotp.TOTP(key)
        return totp.now()
    except TypeError:
        return None


def get(service=None):
    """
    Gets TOTP codes for service specified. If no service is specified it
    it prints codes for all services
    """
    keys = setup_keys()
    if not service:
        for service, value in keys.iteritems():
            totp = get_totp(value)
            if totp:
                print('{}: {}'.format(service, totp))

    elif service in keys:
        totp = get_totp(keys[service])
        if totp:
            print('{}: {}'.format(service, totp))
    else:
        print('{} does not exist'.format(service))


def set(service, key):
    """Accepts a service and a key and saves it out to the keyFile"""
    keys = setup_keys()
    try:
        base64.b32decode(key)
    except TypeError:
        print('{} is not a valid key'.format(key))
    else:
        keys[service] = key
        save_keys(keys)


def rm(service):
    """Accepts a service and removes it from the list of services"""
    keys = setup_keys()
    if keys.pop(service, None):
        print('Removed {}'.format(service))
        save_keys(keys)
    else:
        print('{} does not exist'.format(service))
