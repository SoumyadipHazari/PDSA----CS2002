def special3Bad(L):
    try:
        if L[0] % L[1] == 0 and L[1] != 0:
            if L[0] / (L[1] ** 2 - L[2]) == 0:
                return True
            return False
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except:
        print('Some other exception occured')
    else:
        print('No exception occured')
special3Bad(L)