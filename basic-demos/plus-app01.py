def plus(x,y):
    return x+y

inputs=[];
answer='y'
while answer=='y':
    x=int(input('x?'))
    y=int(input('y?'))
    inputs.append(x)
    inputs.append(y)
    max=plus(x,y)
    print('plus({},{}) =>{}'.format(x,y,max))
    answer=input('continue[y/n] ?')

print('thanks for using the program')
print('max value entered is ',max(inputs))