import math
from functools import lru_cache

def can_i_win(max_choosable, total):
    if total == 0:
        return True

    @lru_cache(None)
    def ciw(leftover, tot, is_player=True):
        if tot >= total:
            if is_player: # opponent made last move, we lose!!
                return -1
            else:
                return 1

        if is_player:
            val = -1
            for l in leftover:
                if ciw(leftover - {l}, tot + l, not is_player) == 1:
                    val = 1
                    break
            return val
        else:
            val = 1
            for l in leftover:
                if ciw(leftover - {l}, tot + l, not is_player) == -1:
                    val = -1
                    break
            return val

    return ciw(frozenset(range(1, max_choosable+1)), 0) == 1


if __name__ == '__main__':
    print(can_i_win(20, 210))



