def drop_last_first(grades):
    # first, middle, last = grades ---causing a “too many values to unpack”
    first, *middle, last = grades #Python “star expressions” can be used to address this problem.
    average = ( first + last ) / 2
    return average

if __name__ == '__main__':
    avg = drop_last_first(range(1,101))
    print(avg)