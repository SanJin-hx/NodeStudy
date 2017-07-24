def sumbif(x):
    result = 0

    for each in x:
        if (type(each) == int) or (type(each) == float):
            result += each
        else:
            continue

    return result