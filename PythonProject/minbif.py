def minbif(x):
    least = x[0]

    for each in x:
        if each < least:
            least = each

    return least
