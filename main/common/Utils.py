import random
import string


class Utils:
    @staticmethod
    def random_string(length):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def random_number(length):
        """Generate a random number of fixed length """
        return ''.join(["{}".format(random.randint(0, 9)) for num in range(0, length)])
