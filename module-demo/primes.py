

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