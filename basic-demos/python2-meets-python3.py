if sys.version_info.major>=3:
        print('please use this script with version 2')
        return
    


import sys

def python2():    
    print('before future import')
    print(1,2,3,4)

def python3():
    from __future__ import print
    print('after future import')
    print(1,2,3,4,sep='\t')

def main():
    python2()
    python3()

main()