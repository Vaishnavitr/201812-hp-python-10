import sys


# if you are running under python 3 (python 2 or lower)
# change your input function to raw_input
if sys.version_info.major<3:
    input=raw_input


def read_int(prompt):
    return int(input(prompt))

def read_str(prompt):
    return input(prompt)


def read_float(prompt):
    return float(input(prompt))

def read_bool(prompt):
    trues=['y','yes','true','ok','fine','done','continue','t']
    ans=input(prompt).lower()
    return ans in trues
