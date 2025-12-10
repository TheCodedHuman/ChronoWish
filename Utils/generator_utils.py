# Imports
from random import choice                               # secrets module would be overkill
from string import ascii_letters, digits

# Character sequence
characters = ascii_letters + digits                     # custom strings can be passed

# Defined
def generate_uid(length: int = 6) -> str:
    """Generates a random sequence of alphabets (A-Z, a-z) and digits (0-9)"""
    
    synthesis = ""                                      # empty string getting appended

    for _ in range(length):
        synthesis += choice(characters)                 # can be optimized by ''.join() method

    return synthesis

