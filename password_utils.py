import string
import secrets

def generate_password(length, use_letters=False, use_digits=False, use_symbols=False, exclude_chars=''):
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    char_pool = ''
    guaranteed = []

    if use_letters:
        char_pool += string.ascii_letters
        guaranteed.append(secrets.choice(string.ascii_letters))
    if use_digits:
        char_pool += string.digits
        guaranteed.append(secrets.choice(string.digits))
    if use_symbols:
        char_pool += string.punctuation
        guaranteed.append(secrets.choice(string.punctuation))

    for char in exclude_chars:
        char_pool = char_pool.replace(char, '')

    if not char_pool:
        raise ValueError("No characters left in the pool after exclusions. Please adjust settings.")

    remaining_length = length - len(guaranteed)
    if remaining_length < 0:
        raise ValueError("Password length too short for selected options.")

    password = guaranteed + [secrets.choice(char_pool) for _ in range(remaining_length)]
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)
