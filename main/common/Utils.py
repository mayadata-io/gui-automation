import random
import string


class Utils:
    @staticmethod
    def random_string(length):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

