import random
import string


def random_string(length=8):
    """
    Generate a random lowercase string of given length.
    Example: 'xjklmqpz'
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def random_email(domain="gmail.com", length=6):
    """
    Generate a random email address.
    Example: 'abxkzr@gmail.com'
    """
    return f"{random_string(length)}@{domain}"
