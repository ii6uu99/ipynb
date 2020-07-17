#!/usr/bin/python

import keyring
import getpass

username=input("Enter username: ")
keyring.set_password("corp", username, getpass.getpass())

password = keyring.get_password("corp", username, getpass.getpass())

print("Password: " + password)