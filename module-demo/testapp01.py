import utils

def main():
    ans=True
    while ans:
        lo=read_int('min?')
        hi=read_int('max?')
        primes=prime_range(lo,hi)
        result=average(*primes)
        print('total primes in range ({}-{}) is {}'.format(lo,hi,len(primes)))

        print('average of {} is {}'.format(primes,result))

        ans=read_bool('continue?')

main()