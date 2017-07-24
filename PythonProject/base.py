def compute(*params,base=3):
    sums = 0
    result = 0
    if params[len(params)-1] == 5:
        base = 5
        sums = sum(params)
        result = sums * base
    else:
        sums = sum(params)
        result = sums*base

    return result

print(compute(1,2,5))