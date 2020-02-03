import operator
from functools import lru_cache
import math


def max_profit_dp_table(prices):
    states = list(range(5))
    NotBought, Bought1, Sold1, Bought2, Sold2 = states
    dp_table = {
        (NotBought, -1): 0,
        (Bought1, -1): -math.inf,
        (Sold1, -1): -math.inf,
        (Bought2, -1): -math.inf,
        (Sold2, -1): -math.inf
    }
    for i, price_now in enumerate(prices):
        for state in states:
            if state == NotBought:
                dp_table[(NotBought, i)] = dp_table[(NotBought, i - 1)]
            if state == Bought1:
                buy_today = dp_table[(NotBought, i - 1)] - price_now
                bought_before = dp_table[(Bought1, i - 1)]
                dp_table[(state, i)] = max(buy_today, bought_before)
            if state == Sold1:
                sell_today = dp_table[(Bought1, i - 1)] + price_now
                sold_before = dp_table[(Sold1, i - 1)]
                dp_table[(state, i)] = max(sell_today, sold_before)
            if state == Bought2:
                buy_today = dp_table[(Sold1, i - 1)] - price_now
                bought_before_today = dp_table[(Bought2, i - 1)]
                dp_table[(state, i)] = max(bought_before_today, buy_today)
            if state == Sold2:
                sell_today = dp_table[(Bought2, i - 1)] + price_now
                sold_before_today = dp_table[(Sold2, i - 1)]
                dp_table[(state, i)] = max(sell_today, sold_before_today)
    last_idx = len(prices) - 1
    return max([dp_table[(s, last_idx)] for s in states ])


def max_profit_generic(prices, k):

    print('')




def max_profit(prices):

    NotBought, Bought1, Sold1, Bought2, Sold2 = list(range(5))

    StartingState = {
        NotBought: 0,
        Bought1: - math.inf,
        Bought2: - math.inf,
        Sold1: - math.inf,
        Sold2: - math.inf
    }

    @lru_cache(None)
    def get_gains(state, i):
        if i == -1:
            return StartingState[state]
        price_now = prices[i]
        if state == NotBought:
            return get_gains(NotBought, i - 1)
        if state == Bought1:
            buy_today = get_gains(NotBought, i - 1) - price_now
            bought_before = get_gains(Bought1, i - 1)
            return max(buy_today, bought_before)
        if state == Sold1:
            sell_today = get_gains(Bought1, i - 1) + price_now
            sold_before = get_gains(Sold1, i - 1)
            return max(sell_today, sold_before)
        if state == Bought2:
            buy_today = get_gains(Sold1, i - 1) - price_now
            bought_before_today = get_gains(Bought2, i - 1)
            return max(bought_before_today, buy_today)
        if state == Sold2:
            sell_today = get_gains(Bought2, i - 1) + price_now
            sold_before_today = get_gains(Sold2, i -1)
            return max(sell_today, sold_before_today)

    return max([get_gains(s, len(prices) - 1) for s in (NotBought, Bought1, Sold1, Bought2, Sold2)])



if __name__ == '__main__':
    print(max_profit_dp_table([1,2,4,2,5,7,2,4,9,0]))
    max_profit_generic([1,2,4,2,5,7,2,4,9,0], 3)
    # print(max_profit([7,6,4,3,1]))
    # print(max_profit([3,3,5,0,0,3,1,4]))
    # print(max_profit([1,2,3,4,5]))

