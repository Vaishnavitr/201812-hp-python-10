 
'''
Here the name u is added to global context but elements within the module
read_int, read_str etc are not added to global context
'''
import utils as u 

'''
only prime_range is added to the context
even the module name primes is NOT added to the context
'''
from primes import prime_range

'''
imports all names from maths (sum and average)
maths itself is not imported
NOTE this code will bring even unwanted names (sum) into global context
This polutes the namespace
'''
from maths import *



def main():
    ans=True
    while ans:
        lo=u.read_int('min?')
        hi=u.read_int('max?')
        primes=prime_range(lo,hi)
        result=average(*primes)
        print('total primes in range ({}-{}) is {}'.format(lo,hi,len(primes)))

        print('average of {} is {}'.format(primes,result))

        ans=u.read_bool('continue?')

if __name__=='__main__':
        main()