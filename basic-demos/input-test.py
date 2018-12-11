
n=int(input('enter number ? '))
fn=1
while n>1:
    fn*=n
    n-=1

print('Factorial is {}'.format(fn))