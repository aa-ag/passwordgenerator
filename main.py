import string
from random import *

characters = string.ascii_letters + string.digits + string.punctuation

password = "".join(choice(characters) for i in range(randint(8, 16)))

print(password)