#https://leetcode.com/problems/remove-boxes/
import functools

def remove_boxes(boxes):

    @functools.lru_cache(None)
    def remove(i, j):
        all_equal = True
        for k in range(i, j):
            if boxes[k] != boxes[k+1]:
                all_equal = False
        if all_equal:
            length = j - i + 1
            print(f'{i}-{j}: {length**2}')
            return length ** 2
        best = 0
        for p1 in range(i, j):
            for p2 in range(p1, j):
                if i == 1 and j == 3 and p1 == 2 and p2 == 2:
                    print('cond')
                cost_merge = remove(p1, p2)
                consec_count = 0
                last = None
                cost_rest = 0
                for k in range(i, j+1):
                    if k >= p1 and k <= p2:
                        continue
                    if boxes[k] == last:
                        consec_count += 1
                        if consec_count == 1:
                            cost_rest -= 1
                    else:
                        if consec_count > 0:
                            cost_rest += (consec_count+1) ** 2
                        consec_count = 0
                        cost_rest += 1
                    last = boxes[k]
                add = 0
                if consec_count > 0:
                    add = (consec_count + 1) ** 2
                best = max(best, cost_merge + cost_rest + add)
        print(f'best {i}-{k}: {best}')
        return best

    return remove(0, len(boxes) - 1)


if __name__ == '__main__':
    print(remove_boxes([ 3, 2, 2, 2, 3, 4, 3]))