import sys
import ca.console.v2.utils as v2
import ca.console.v3.utils as v3



# if you are running under python 3 (python 2 or lower)
# change your input function to raw_input
if sys.version_info.major<3:
    read_str=v2.read_str
else:
    read_str=v3.read_str


def read_int(prompt):
    return int(read_str(prompt))

#def read_str(prompt):
#    return input(prompt)


def read_float(prompt):
    return float(read_str(prompt))

def read_bool(prompt):
    trues=['y','yes','true','ok','fine','done','continue','t']
    ans=read_str(prompt).lower()
    return ans in trues
