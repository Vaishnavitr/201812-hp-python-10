

def sum(*args):
    result=0
    for value in args:
        result+=value
    return result


def average(*args):
    return sum(*args)/len(args)


def main():
    print('testing maths module functions')
    
    print('should be 10',sum(1,2,3,4))
    #print('should be 5050', sum(n for n in range(1,101)))
    print('should be 10', average(9,10,11))
    print('maths test ended')


if __name__=='__main__':
    print('maths module name is ',__name__)
    main()