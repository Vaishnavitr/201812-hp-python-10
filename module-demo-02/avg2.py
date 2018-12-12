import sys

def main(args):
    sum=0
    for value in args:
        sum+=float(value)

    print(sum/len(args))


if __name__=='__main__':
    main( sys.argv[1:])