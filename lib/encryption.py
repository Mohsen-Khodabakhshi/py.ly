from string import ascii_letters, digits

from random import choice


def new_short_url_generator(length: int = 5):
    """this function will create a random string with a-z, A-Z, 0-9

    Args:
        length (int, optional): length of output string. Defaults to 5.

    Returns:
        string: this is generated random string
    """
    characters = ascii_letters + digits
    random_string = ''.join(choice(characters) for _ in range(length))
    return random_string
