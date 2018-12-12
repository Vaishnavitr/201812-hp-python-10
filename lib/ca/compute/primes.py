

def is_prime(number):
    if number<0 : number*=-1
    if number<2 : return False
    
    for x in range(2,number):
        if number%x==0:
            return False

    return True

def prime_range(min,max=None):
    result=[]
    if max==None:
        min,max=0,min

    for value in range(min,max):
        if is_prime(value):
            result.append(value)

    return result

def test():
    print('testing primesmodule')

    print('is_prime(2)',is_prime(2))
    print('is_prime(3)',is_prime(3))
    print('is_prime(5)',is_prime(5))
    print('is_prime(9)',is_prime(9))
    print('is_prime(-4)',is_prime(-4))

    print('prime_range(1,10)',prime_range(1,10))
    print('prime_range(10,20)',prime_range(10,20))


    print('--end of test--')


#print('primes module name is ',__name__)
# run below code only when executed directly and not when imported
if __name__=='__main__':
    
    test()