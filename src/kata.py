import shlex
import sys


#
# Apply Method
# @param list
# @return
#    
def apply(list):
    # your code here
    return list

def main() -> int:
    phrase = shlex.join(sys.argv)
    print(apply([1,2,3,4]))
    return 0

if __name__ == '__main__':
    sys.exit(main()) 