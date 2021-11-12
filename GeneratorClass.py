import random
import time

class number_generator:
    def __init__(self, amount, minnr, maxnr):
        self.amount = amount
        self.minnr = minnr
        self.maxnr = maxnr

    def generator(self):
        c = self.amount
        f = 0
        assert isinstance(self.amount, int) \
               and isinstance(self.minnr, int) \
               and isinstance(self.maxnr, int), \
            'amount, minnr, and maxnr must be ' \
            'integers. please try again'
        assert self.minnr < self.maxnr, \
            'minnr cannot be larger than maxnr. ' \
            'please try again'
        while c > 0:
            r = random.randint(self.minnr, self.maxnr)
            c -= 1
            f += 1
            print(r)
            time.sleep(1)
            assert self.minnr <= r <= self.maxnr, \
                'a number lower or higher than allowed' \
                'was generated. please try again'
        assert self.amount == f, \
            'amount of random numbers generated were' \
            ' not the same as specified amount.' \
            ' please try again'


example = number_generator(5,1,6)
example.generator()
