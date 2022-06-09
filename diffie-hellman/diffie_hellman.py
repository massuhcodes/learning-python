# generate a shared secret key - https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

import secrets

def private_key(p):
    """Pick a private key that is greater than 1 and less then p
    :param p: int - a prime number
    :return: int - a random number chosen to be a private key
    """
    return secrets.choice(range(2,p))


def public_key(p, g, private):
    """Calculate a public key using the private key
    :param p: int - a prime number
    :param g: int - another prime number
    :return: int - the calculated private key
    """
    return pow(g, private) % p


def secret(p, public, private):
    """Calculate a secret key using both public and private keys
    :param public: int - calculated from public_key function
    :param private: int - calculated from private_key function
    :return: int - the shared secret key 
    """
    
    return pow(public, private) % p
