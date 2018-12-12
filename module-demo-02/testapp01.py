import utils
import primes as p #call this module p
from maths import average


def main():
    ans=True
    print('welcome to module ',__name__)
    while ans:
        lo=utils.read_int('min?')
        hi=utils.read_int('max?')
        primes=p.prime_range(lo,hi)
        result=average(*primes)
        print('total primes in range ({}-{}) is {}'.format(lo,hi,len(primes)))

        print('average of {} is {}'.format(primes,result))

        ans=utils.read_bool('continue?')

if __name__=='__main__':
        main()