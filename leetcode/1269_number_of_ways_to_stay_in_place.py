import functools


def num_ways(steps, arrlen):

    to_mod = 10**9 + 7

    @functools.lru_cache(None)
    def nways(pos, step):
        if pos < 0 or pos >= arrlen:
            return 0
        if step == 0:
            if pos == 0:
                return 1
            else:
                return 0
        else:
            return (nways(pos, step - 1) +
                    nways(pos + 1, step - 1) +
                    nways(pos - 1, step - 1))

    return nways(0, steps) % to_mod

if __name__ == '__main__':
    print(num_ways(2, 4))


