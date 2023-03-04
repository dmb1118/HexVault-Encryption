import math
import random

# Global Declarations
organized_master_list = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_+=;:,<.>'\"\\{}[]/?"
master_list = "W,v4M_kY5I.$Cct3^rB>96gFE\"j?'eQm8:K#(ZJ+&;2q=-7Uf)lbD*uH!X[0%A xpsw@ha1NG<yidzSPTV/O]no\\}LR{"
# The master list was randomized to prevent patterns from forming to allow greater encryption randomisation
CONST = 2121999  # Const value set by user for stable calculation
encryption_key = ""

key_constants = {
    'L1a': 2,
    'L1b': 3,
    'L1c': 5,
    'L1d': 7,
    'L1e': 11,
    'L1f': 13,
    'L2a': 211,
    'L2b': 223,
    'L2c': 227,
    'L2d': 229,
    'L2e': 233,
    'L2f': 239,
    'L3a': 401,
    'L3b': 409,
    'L3c': 419,
    'L3d': 421,
    'L3e': 431,
    'L3f': 433,
    'L4a': 601,
    'L4b': 607,
    'L4c': 613,
    'L4d': 617,
    'L4e': 619,
    'L4f': 631,
    'L5a': 809,
    'L5b': 811,
    'L5c': 821,
    'L5d': 823,
    'L5e': 827,
    'L5f': 829,
    'L6a': 1009,
    'L6b': 1013,
    'L6c': 1019,
    'L6d': 1021,
    'L6e': 1031,
    'L6f': 1033,
}
key_constants_list = ['L1a', 'L1b', 'L1c', 'L1d', 'L1e', 'L1f', 'L2a', 'L2b', 'L2c', 'L2d', 'L2e', 'L2f', 'L3a', 'L3b',
                      'L3c', 'L3d', 'L3e', 'L3f', 'L4a', 'L4b', 'L4c', 'L4d', 'L4e', 'L4f', 'L5a', 'L5b', 'L5c', 'L5d',
                      'L5e', 'L5f', 'L6a', 'L6b', 'L6c', 'L6d', 'L6e', 'L6f']


def rng(num):
    """Generates a random number between 0 and a number given"""
    return random.randint(0, num)


def find_digit_score(digit):
    """Gives a trackable value for each letter, number, and special character"""
    value = 0
    for item in master_list:
        if digit == item:
            value = master_list.index(item) + 1
    return value


def find_index_from_score(digit_score):
    """Takes the inherent assigned value and returns the list index from the value given"""
    return int(digit_score) - 1


def encrypt_digit(digit, count, key_const_copy):
    """Allows you to return an encrypted digit based on the input digit of a string"""
    digit_score = find_digit_score(digit)
    current_key = key_const_copy[count - 1]
    # print(f"Digit: {digit}, Digit Score: {digit_score}, Const: {CONST}, Current Key: {current_key}, Current Key Val {key_constants[current_key]}")
    e_digit = str((digit_score * CONST * key_constants[current_key]))
    return e_digit


def decrypt_digit(current_key, e_digit):
    """Allows you to return an unencrypted digit when you input an encrypted digit number and the appropriate key"""
    e_digit = int(e_digit)
    current_key.split()
    digit_score = e_digit / CONST / key_constants[current_key]
    # print(f"E Digit: {e_digit}, Digit Score: {digit_score}, Const: {CONST}, Current Key: {current_key}, Current Key Val {key_constants[current_key]}")
    digit_index = find_index_from_score(digit_score)
    digit = master_list[digit_index]
    return digit
