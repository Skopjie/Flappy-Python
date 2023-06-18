import random

class RandomUtils:
    @staticmethod
    def get_random_number_btw_range(min, max):
       random_number = random.randint(min, max)
       return random_number