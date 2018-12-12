def plus(x,y):
    return x+y

inputs=[];
def main_loop():
    answer='y'
    while answer=='y':
        x=int(input('x?'))
        y=int(input('y?'))
        inputs.append(x)
        inputs.append(y)
        max=plus(x,y)
        print('plus({},{}) =>{}'.format(x,y,max))
        answer=input('continue[y/n] ?')

def main():
    main_loop()
    print('thanks for using the program')
    print('max value entered is ',max(inputs))

main()