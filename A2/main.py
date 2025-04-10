# program to check if the Nth bit set or not
def setOrNot(number, n):
    # make a mask variable by left shifting 1 (k-1) times and check if (n AND mask) equals 1 or 0
    if number & (1 << (n - 1)):
        print( "\nSET")
    else:
        print( "\nNOT SET")
number = int(input("Enter your number : "))
n = int(input("Enter your Bit position : "))
setOrNot(number, n)
    