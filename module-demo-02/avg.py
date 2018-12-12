import sys

def main(appname, *args):
    sum=0
    for value in args:
        sum+=float(value)

    print(sum/len(args))


if __name__=='__main__':
    main(* sys.argv)