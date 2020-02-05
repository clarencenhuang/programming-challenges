import math
from functools import lru_cache

def guess_number(n):

    @lru_cache(None)
    def do_guess(low, hi):
        if low == hi:
            return 0
        best_guess = math.inf
        for num in range(low, hi+1):
            guesses = []
            if num > low:
                guesses.append(num + do_guess(low, num - 1))
            if num < hi:
                guesses.append(num + do_guess(num + 1, hi))
            best_guess = min(best_guess, max(guesses))

        return best_guess

    return do_guess(1, n)


if __name__ == '__main__':
    print(guess_number(20))


