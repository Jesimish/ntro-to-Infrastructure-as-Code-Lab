#!/usr/bin/env python3

# in this file I'm going to practice the structure of python commands

# First you need to import your modules that you will use in this function. 
# There will be a Random and string Module. I will need to add an attribute to the string module to allow uppercase and lowercase letters.

import clipman
import random
import string
import subprocess

# Before using clipman, you must initialize it
clipman.init()

def random_password(length):
    if length < 8:
        raise ValueError("😬 Sorry... your password must be at least 8 characters long.")
    
    # I need to make sure we have at least one upper and lower letter and numbers. 
    # Ideally I'd like it to include a special character so I'll try and figure that out.

    # --- Character sets from string module ---
    # string.ascii_lowercase → all lowercase letters
    # string.ascii_uppercase → all uppercase letters
    # string.ascii_letters   → all letters (uppercase and lowercase)
    # string.digits          → all digit characters (0–9)
    # string.punctuation     → all special symbol characters

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # I need to combine them
    all_chars = letters + digits + symbols

    # Randomly select characters from all_chars
    password_chars = random.choices(all_chars, k=length)

    # The line before this will generate the pieces but they need to be combined so I'll have to use join.
    return ''.join(password_chars)

def store_password_in_pass(entry_name, password):
    try:
        # Use subprocess to call: pass insert --multiline entry_name
        subprocess.run(
            ["pass", "insert", "--multiline", entry_name],
            input=password.encode(),
            check=True
        )
        print(f"💫 Password stored securely as: {entry_name}")
    except subprocess.CalledProcessError as e:
        print("💃 Error storing password in pass:", e)

try:
    user_input = input("How long do you want your password? ")
    length = int(user_input)
    
    password = random_password(length)
    print("Here is your password:", password)

    # Copy the password to clipboard using clipman
    clipman.copy(password)
    print("✅ Password copied to clipboard! Just a reminder, you are so smart and secure🥰")

    # Ask for an entry name for storing the password locally in Pass
    save = input("Do you want to store this password in your password manager? (y/n): ").lower()
    if save == "y":
        entry_name = input("What should we call this entry (e.g., github.com/email)? ")
        store_password_in_pass(entry_name, password)

except ValueError:
    print("😬 Ooops! Please enter a valid number greater than 8.")
