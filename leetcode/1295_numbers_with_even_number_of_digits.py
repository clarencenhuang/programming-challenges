

def even_digits(nums):
    num_digits = [1 for x in nums if len(str(x)) % 2 == 0]
    return len(num_digits)