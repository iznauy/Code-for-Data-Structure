def knap_rec(weight, wlist, n):
    if weigth == 0:
        return True
    if weight < 0 or (weight > 0 and n < 1):
        return False
    if knap_rec(weight-wlist[n-1], wlist, n-1):
        print 'Item ' + str(n) + ":" + wlist[n-1]
        return True
    if knap_rec(weight, wlist, n-1):
        return True

    return False
