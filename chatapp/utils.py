import random
import string

rooms = {}


def generate_unique_code(length: int) -> str:
    """Generate code."""
    while True:
        code = ''
        for _ in range(length):
            code += random.choice(string.ascii_uppercase)

        if code not in rooms:
            break

        return code
