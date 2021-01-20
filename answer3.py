def noRecur(n, cur=0):
    if n < 2:
        raise 'Invaild input'
    else:
        while n >= 2:
            if n == 2:
                return 1 / n + cur
            else:
                cur += 1 / (n * (n - 1))
                n -= 1