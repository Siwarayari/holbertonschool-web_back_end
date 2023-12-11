#!/usr/bin/env python3
"""Implement a hash_password function that expects
one string argument name password and returns a salted,
hashed password, which is a byte string"""


import bcrypt


def hash_password(password: str) -> bytes:
    """Implement a hash_password function that expects
one string argument name password and returns a salted,
hashed password, which is a byte string"""
    password = password.encode('utf-8')
    mySalt = bcrypt.gensalt()
    pwd_hash = bcrypt.hashpw(password, mySalt)
    return (pwd_hash)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Implement an is_valid function that
expects 2 arguments and returns a boolean"""
    password = password.encode('utf-8')
    pwd_hash = bcrypt.checkpw(password, hashed_password)
    return (pwd_hash)
