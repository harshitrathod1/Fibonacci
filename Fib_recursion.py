def fibr(n):
    if n==0 or n==1:
        return n
    else:
        return fibr(n-1)+fibr(n-2)
