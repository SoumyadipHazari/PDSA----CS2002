def isSymmetricBad(L):
    try:
        while len(L) > 0:
            if L.pop(0) != L.pop(-1):
                return False
            return True
    except IndexError:
        print('IndexError')
    except:
        print('Some other exception occured')
    else:
        print('No exception occured')
isSymmetricBad(L)