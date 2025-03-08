def fibonanaci_sum_navie(from_, to):
    _sum = 0
    previous = 0
    current = 1
    for i in range(to+1):
        if i>=from_:
            _sum += previous
        previous,current = current,previous+current
    return _sum%10
