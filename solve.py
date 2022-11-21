def solve(n, repeats):
    sum_ = 0
    while repeats != 0:
        sum_ += int(str(n) * repeats)
        repeats -= 1
    return sum_
