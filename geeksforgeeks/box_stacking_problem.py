import itertools

def process_boxes(boxes):
    effective_boxes = set()
    for i in itertools.islice(range(len(boxes)), 0, None, 3):
        l, w, h = boxes[i:i + 3]
        effective_boxes.add((l * w, l, w, h))
        effective_boxes.add((w * h, w, h, l))
        effective_boxes.add((l * h, l, h, w))
    dims = [(b1, b2, h) for _, b1, b2, h in reversed(sorted(effective_boxes))]
    return dims

def box_stacker_max(boxes):
    dims = process_boxes(boxes)
    def max_height(i):
        if i < 0:
            return 0
        b1, b2, h = dims[i]
        h_so_far = h
        for k in range(i-1, -1, -1):
            pb1, pb2, _ = dims[k]
            if pb1 > b1 and pb2 > b2:
                h_so_far = max(h_so_far, max_height(k) + h)
                break
        h_so_far = max(h_so_far, max_height(i-1)) # if we dont include self
        return h_so_far
    return max_height(len(dims) - 1)


def box_stacker(boxes):
    dims = process_boxes(boxes)
    
    def do_stack(i):
        b1, b2, h = dims[i]
        h_so_far = h # we can always use the box itself, this is also the terminate condition
        for k in range(0, i):
            pb1, pb2, _ = dims[k]
            if pb1 > b1 and pb2 > b2:
                h_so_far = max(h_so_far, do_stack(k) + h)
        return h_so_far

    return do_stack(len(dims) - 1)


def box_stacker_dp(boxes):
    pass


if __name__ == '__main__':
    boxes = list(map(int, '4 6 7 1 2 3 4 5 6 10 12 32'.split()))
    print(box_stacker_max(boxes))
